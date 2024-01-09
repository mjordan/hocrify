# Hocrify

A script to generate hOCR using Tesseract on a directory of TIFF files. Proof of concept at the moment, but once we figure out our requirements, we can modify the script as needed.

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
Also provides the option to create an OCR file, which just contains the extracted text content:

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

## Configuration and usage

You will need to conigure the following four variables at the top of the script:

* `input_dir`: the path to the page images, organized by book or newspaper issue.
* `output_dir`: where to save the output. If left empty (`''`), the input_dir will be used.
* `page_image_extension`: the extension of the source page image file, without the leading period, e.g. `tif`.
* `filename_segment_separator`: the character used to separate the page number from the rest of the page image file, e.g. the `-` that separates the `02` from `1948-11-12` in `1948-11-12-02.tif`. Does not need to be the same as the separator used in the non-page number part of the filename. It also doesn't matter what comes before the page number separator.
* `generate_ocr`: set to `True` to extract the text from the hOCR, producing the equivalent of an OCR file with no line breaks.
* `log_file_path`: the path to your log file.
* `pytesseract.pytesseract.tesseract_cmd`: the full path to the Tesseract executable, if necessary.

## Requirements

- Tesseract
- [pytesseract](https://pypi.org/project/pytesseract/)
