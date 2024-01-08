import os
import pytesseract

input_dir = 'input'
page_image_extension = 'tif'

# Could be books or newspaper issues.
page_containers = os.listdir(input_dir)

for page_container in page_containers:
    pages = os.listdir(os.path.join(input_dir, page_container))

    for page in pages:
        if page.endswith(page_image_extension):
            page_image_filepath = os.path.join(input_dir, page_container, page)
            page_image_filepath_without_extension = os.path.splitext(page_image_filepath)[0]
            page_hocr_filepath = os.path.join(page_image_filepath_without_extension + '.hocr')

            try:
                # Generate hOCR and save it.
                print(f"Generating hOCR from {page}... ", end='')
                hocr_content = pytesseract.image_to_pdf_or_hocr(page_image_filepath, extension='hocr')
                hocr_file = open(page_hocr_filepath, 'wb+')
                hocr_file.write(hocr_content)
                hocr_file.close
                print("done.")
            except Exception as e:
                print(f'Error: {e}')



