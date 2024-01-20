import os
import sys
import re
import shutil
import logging
import time
from multiprocessing import Process

import pytesseract
from bs4 import BeautifulSoup

###########################
# Configuration varaibles #
###########################

input_dir = 'input'
# Leave 'output_dir' empty ('') to write output back into input_dir.
output_dir = 'output'
page_image_extension = 'tif'
hocr_extension = 'hocr'
ocr_extension = 'txt'
source_language = 'eng'
filename_segment_separator = '-'
# Set 'generate_ocr' to False to only generate hOCR for each page.
generate_ocr = True
log_file_path = 'tesseract.log'

# If you don't have tesseract executable in your system's PATH, uncomment this next
# variable and specify the path to the tesseract executable.
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Leave 'do_invert' as is unless your page images contain substantial amounts
# of text in more than one language. If the accuracy of the OCR in your additional
# language text is very poor, you should change this to ' tessedit_do_invert=1',
# but doing so will come with a hit to processing speed.
do_invert = ' tessedit_do_invert=0'

############################################
# You do not need to change anything below #
############################################

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S')

if not os.path.exists(input_dir):
    message = f'Error: cannot find input directory "{input_dir}".'
    logging.error(message)
    sys.exit(message)

tesseract_version = pytesseract.pytesseract.get_tesseract_version()

if generate_ocr is True:
    generate_ocr_message = f"and OCR"
else:
    generate_ocr_message = ''
if len(output_dir) > 0:
    start_message = f"hocrify job started (hOCR {generate_ocr_message}), using page images from {os.path.abspath(input_dir)} and saving output to {os.path.abspath(output_dir)} (tesseract version {tesseract_version})."
else:
    start_message = f"hocrify job started (hOCR {generate_ocr_message}), using page images from {os.path.abspath(input_dir)} and saving output to the source directory (tesseract version {tesseract_version})."
logging.info(start_message)

# Could be books or newspaper issues.
page_containers = os.listdir(input_dir)

def generate_output(oddeven):
    for page_container in page_containers:
        if len(output_dir) > 0:
            if not os.path.exists(os.path.join(output_dir, page_container)):
                os.mkdir(os.path.join(output_dir, page_container))

        pages = os.listdir(os.path.join(input_dir, page_container))

        for page in pages:
            timer_start = time.perf_counter()
            # We distinguish between odd an even pages so each of out two processes don't step on each other.
            filename_segments = os.path.splitext(page)[0].split(filename_segment_separator)
            order_segment = filename_segments[-1]
            if int(order_segment) % 2 == 0 and oddeven == 'odd':
                continue
            if int(order_segment) % 2 != 0 and oddeven == 'even':
                continue

            if page.endswith('.' + page_image_extension):
                page_image_filepath = os.path.join(input_dir, page_container, page)
                if len(output_dir) > 0:
                    shutil.copyfile(page_image_filepath, os.path.join(output_dir, page_container, page))
                page_image_filepath_without_extension = os.path.splitext(page_image_filepath)[0]
                if len(output_dir) > 0:
                    page_hocr_filepath = os.path.join(output_dir, page_container, os.path.splitext(page)[0] + '.' + hocr_extension)
                    page_ocr_filepath = os.path.join(output_dir, page_container, os.path.splitext(page)[0] + '.' + ocr_extension)
                else:
                    page_hocr_filepath = os.path.join(page_image_filepath_without_extension + '.' + hocr_extension)
                    page_ocr_filepath = os.path.join(page_image_filepath_without_extension + '.' + ocr_extension)

                try:
                    # Generate hOCR and save it to a file.
                    hocr_content = pytesseract.image_to_pdf_or_hocr(page_image_filepath, extension='hocr', lang=source_language, config=do_invert)
                    hocr_file = open(page_hocr_filepath, 'wb+')
                    hocr_file.write(hocr_content)
                    hocr_file.close
                except Exception as e:
                    logging.error(f'Error generating hOCR: {e}')
                    print(f'Error generating hOCR: {e}')

                # Extract word content from hOCR and save it to a file.
                if generate_ocr is True:
                    try:
                        soup = BeautifulSoup(hocr_content, 'html.parser')
                        page_text = soup.findAll(text=True)
                        ocr_content = ' '.join(page_text)
                        ocr_content = re.sub('\n', '', ocr_content)
                        ocr_content = re.sub('^.*transitional.dtd"', '', ocr_content)
                        ocr_content = re.sub(' +', ' ', ocr_content)
                        ocr_file = open(page_ocr_filepath, 'w+')
                        ocr_file.write(ocr_content.strip())
                        ocr_file.close
                    except Exception as e:
                        logging.error(f'Error generating OCR: {e}')
                        print(f'Error generating OCR: {e}')

                timer_end = time.perf_counter()

                page_message = f"Generated hOCR {generate_ocr_message} from {page} in {timer_end - timer_start:0.1f} seconds."
                logging.info(page_message)
                print(page_message)

if __name__ == "__main__":
    if len(output_dir) > 0 and not os.path.exists(output_dir):
        os.mkdir(output_dir)

    process_odd = Process(target=generate_output, args=('odd',))
    process_odd.start()
    process_odd.join()

    process_even = Process(target=generate_output, args=('even',))
    process_even.start()
    process_even.join()

    logging.info(f"hocrify job completed.")
