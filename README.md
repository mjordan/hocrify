# Hocrify

A script to generate hOCR, and optionally OCR, on a directory of page image files using Tesseract.

For example, if you have a directory of files grouped by newspaper issue, like this:

```
input/
├── 1948-10-07
│   ├── 1948-10-07-01.tif
│   ├── 1948-10-07-02.tif
│   ├── 1948-10-07-03.tif
│   └── 1948-10-07-04.tif
└── 1948-11-12
    ├── 1948-11-12-01.tif
    ├── 1948-11-12-02.tif
    ├── 1948-11-12-03.tif
    └── 1948-11-12-04.tif

```

and run hocrify.py on it, you'll get this:

```
input/
├── 1948-10-07
│   ├── 1948-10-07-01.hocr
│   ├── 1948-10-07-01.tif
│   ├── 1948-10-07-02.hocr
│   ├── 1948-10-07-02.tif
│   ├── 1948-10-07-03.hocr
│   ├── 1948-10-07-03.tif
│   ├── 1948-10-07-04.hocr
│   └── 1948-10-07-04.tif
└── 1948-11-12
    ├── 1948-11-12-01.hocr
    ├── 1948-11-12-01.tif
    ├── 1948-11-12-02.hocr
    ├── 1948-11-12-02.tif
    ├── 1948-11-12-03.hocr
    ├── 1948-11-12-03.tif
    ├── 1948-11-12-04.hocr
    └── 1948-11-12-04.tif
```
Hocrify also provides the option to create an OCR file, which just contains the extracted text content (Hocrify doesn't reprocess the input image):

```
input/
├── 1948-10-07
│   ├── 1948-10-07-01.hocr
│   ├── 1948-10-07-01.tif
│   ├── 1948-10-07-01.txt
│   ├── 1948-10-07-02.hocr
│   ├── 1948-10-07-02.tif
│   ├── 1948-10-07-02.txt
│   ├── 1948-10-07-03.hocr
│   ├── 1948-10-07-03.tif
│   ├── 1948-10-07-03.txt
│   ├── 1948-10-07-04.hocr
│   ├── 1948-10-07-04.tif
│   └── 1948-10-07-04.txt
└── 1948-11-12
    ├── 1948-11-12-01.hocr
    ├── 1948-11-12-01.tif
    ├── 1948-11-12-01.txt
    ├── 1948-11-12-02.hocr
    ├── 1948-11-12-02.tif
    ├── 1948-11-12-02.txt
    ├── 1948-11-12-03.hocr
    ├── 1948-11-12-03.tif
    ├── 1948-11-12-03.txt
    ├── 1948-11-12-04.hocr
    ├── 1948-11-12-04.tif
    └── 1948-11-12-04.txt
```

## Usage

Once configured (see next section), you run the script like this:

`python hocrify.py`

This script is not fast. It is optimized to run two parallel processes (one for odd numbered pages and one for even numbered pages) but it's still not very fast. If you have a lot of pages to process, you may want to consider running the script on multiple computers at one time.

## Configuration

You will need to configure the following four variables at the top of the script:

* `input_dir`: the path to the page images, organized by book or newspaper issue.
* `output_dir`: where to save the output, including a copy of the input page image files. If left empty (`''`), the input_dir will be used.
* `page_image_extension`: the extension of the source page image file, without the leading period, e.g. `tif`.
* `filename_segment_separator`: the character used to separate the page number from the rest of the page image file, e.g. the `-` that separates the `02` from `1948-11-12` in `1948-11-12-02.tif`. Does not need to be the same as the separator used in the non-page number part of the filename. It also doesn't matter what comes before the page number separator.
* `generate_ocr`: set to `True` to extract the text from the hOCR, producing the equivalent of an OCR file with no line breaks.
* `log_file_path`: the path to your log file.
* `pytesseract.pytesseract.tesseract_cmd`: the full path to the Tesseract executable file. Whether this is necessary will depend on the computer the script is running on.

## Requirements

- Tesseract
- [pytesseract](https://pypi.org/project/pytesseract/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
