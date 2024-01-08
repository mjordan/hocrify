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

## Requirements

- Tesseract
- [pytesseract](https://pypi.org/project/pytesseract/)
