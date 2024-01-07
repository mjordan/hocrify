import os
import tempfile
import requests
import pytesseract

image_urls_file = 'urls.txt'
output_dir = 'output'

with open(image_urls_file) as iuf:
    image_urls = iuf.read().splitlines()

filename_counter = 0
for image_url in image_urls:
    filename_counter += 1
    image_temp_path = os.path.join(tempfile.gettempdir(), str(filename_counter) + '.tif')
    print(f"Downloading {image_url}...", end='')
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        # Get the page image file and save it.
        image_file = open(image_temp_path, 'wb+')
        image_file.write(response.content)
        image_file.close

        # Generate hOCR and save it.
        hocr_output_path = os.path.join(output_dir, str(filename_counter) + '.hocr')
        print("Generating hOCR...", end='')
        hocr_content = pytesseract.image_to_pdf_or_hocr(image_temp_path, extension='hocr')
        hocr_file = open(hocr_output_path, 'wb+')
        hocr_file.write(hocr_content)
        hocr_file.close
        print("Done.")

        # Delete the page image file.
        if os.path.exists(image_temp_path):
            os.remove(image_temp_path)

