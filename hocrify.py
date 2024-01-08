import os
import re
import pytesseract
from bs4 import BeautifulSoup

input_dir = 'input'
page_image_extension = 'tif'
generate_ocr = True

# Could be books or newspaper issues.
page_containers = os.listdir(input_dir)

for page_container in page_containers:
    pages = os.listdir(os.path.join(input_dir, page_container))

    for page in pages:
        if page.endswith(page_image_extension):
            page_image_filepath = os.path.join(input_dir, page_container, page)
            page_image_filepath_without_extension = os.path.splitext(page_image_filepath)[0]
            page_hocr_filepath = os.path.join(page_image_filepath_without_extension + '.hocr')
            page_ocr_filepath = os.path.join(page_image_filepath_without_extension + '.txt')

            try:
                # Generate hOCR and save it to a file.
                if generate_ocr is True:
                    ocr_message = 'and OCR'
                else:
                    ocr_message = ''
                print(f"Generating hOCR {ocr_message} from {page}... ", end='')
                hocr_content = pytesseract.image_to_pdf_or_hocr(page_image_filepath, extension='hocr')
                hocr_file = open(page_hocr_filepath, 'wb+')
                hocr_file.write(hocr_content)
                hocr_file.close
                print("done.")
            except Exception as e:
                print(f'Error generating hOCR: {e}')

            # Extract word content from hOCR and save it to a file.
            if generate_ocr is True:
                try:
                    soup = BeautifulSoup(hocr_content, features='xml')
                    page_text = soup.findAll(text=True)
                    ocr_content = ' '.join(page_text)
                    ocr_content = re.sub('\n', '', ocr_content)
                    ocr_content = re.sub('html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"', '', ocr_content)
                    ocr_content = re.sub(' +', ' ', ocr_content)
                    ocr_file = open(page_ocr_filepath, 'w+')
                    ocr_file.write(ocr_content)
                    ocr_file.close
                except Exception as e:
                    print(f'Error generating OCR: {e}')

