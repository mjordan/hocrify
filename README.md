# Hocrify

A Python script to generate [hOCR](https://en.wikipedia.org/wiki/HOCR) and [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) on a directory of page image files using [Tesseract](https://tesseract-ocr.github.io/tessdoc/).

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

Hocrify also provides the option to create an OCR file for each page image, which contains the extracted text content (Hocrify doesn't reprocess the input image):

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
Usage is not limited to newspaper issues. Any paged item will work as long as page images in the item are in a single directory under 'input':

```
input/
├── book1
│   ├── page-01.tif
│   ├── page-02.tif
│   ├── page-03.tif
│   └── page-04.tif
└── book_2
    ├── page-01.tif
    ├── page-02.tif
    ├── page-03.tif
    ├── page-04.tif
    ├── page-05.tif
    └── page-06.tif
```

## Usage

Once configured (see next section), you run the script like this:

`python hocrify.py`

## Configuration

You will need to configure the following four variables at the top of the script:

* `input_dir`: the path to the page images, organized by book or newspaper issue.
* `output_dir`: where to save the output, including a copy of the input page image files. If left empty (`''`), output will be written back to `input_dir`. If the output directory doesn't exist, it will be created.
* `page_image_extension`: the extension of the source page image file, without the leading period, e.g. `tif`.
* `filename_segment_separator`: the character used to separate the page number from the rest of the page image file, e.g. the `-` that separates the `02` from `1948-11-12` in `1948-11-12-02.tif`. Does not need to be the same as the separator used in the non-page number part of the filename. It also doesn't matter what comes before the page number separator.
* `generate_hocr`: set to `True` to generate hOCR from the page images, `False` to not generate it.
* `generate_ocr`: set to `True` to extract the text from the hOCR, producing the equivalent of an OCR file with no line breaks. Set to `False` to not create OCR.
* `log_file_path`: the path to your log file.
* `source_language`: language of the source material. Common languages are 'eng', 'fre' and 'chi_sim'. Note that not all language packs may be installed on a given computer. Run `tesseract --list-langs` to see those installed.
* `pytesseract.pytesseract.tesseract_cmd`: the full path to the Tesseract executable file. Whether this is necessary will depend on the computer the script is running on.
* `config_options`: some Tesseract configuration options to increase page-processing speed. You can try adding others if you can find them; these configuration options aren't well documented, especially for Tesseract 4 and 5.

## Performance

The amount of time hocrify takes to process a single page image is determined by a few factors. Ways you can make it faster include:

- Use Tesseract 5. It is substantially faster than Tesseract 4.
- Generating OCR is very CPU-intensive. Therefore, you will get faster results running this script on computers with fast CPUs.
- Keep the `do_invert` and `OMP_THREAD_LIMIT` configuration variables as configured.

## Requirements

- Python
- [Tesseract](https://tesseract-ocr.github.io/tessdoc/) version 5. Version version 4 will work but it is slower than version 5.
- [pytesseract](https://pypi.org/project/pytesseract/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

# License

The Unlicense.

