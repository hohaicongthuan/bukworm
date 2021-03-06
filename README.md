# bukworm

> Đọc bản Tiếng Việt của file `README.md` này [ở đây](README_vi_VN.md)

A highly customisable ebook reader.

***IMPORTANT NOTE: THE PROJECT IS CURRENTLY UNDER DEVELOPMENT AND IS NOT READY FOR USE.***

## Future features plan
- Support viewing PDF files
- Support viewing Microsoft Document files (DOCX, PPTX, XLSX)
- Support viewing Markdown files
- Support viewing common image files (JPG, PNG, QOI, and probably more)
- Allow users to customise font type, font size, font colour, page colour, background colour, and probably more.

## Screenshots

TODO

## Prerequisites

Bukworm requires `Python 3.7` or later, `PIP`, and `virtualenv` installed.

### On Linux-based operating systems

`virtualenv` can be installed using:

```
pip3 install virtualenv
```

### On Windows

_Microsoft Edge WebView 2 Runtime_ is also required. If you're using Windows 10, it's probably already installed on your system. If you're using Windows 7, you can download it [here](https://developer.microsoft.com/en-us/microsoft-edge/webview2/#download-section) (_Evergreen Standalone Installer_ is recommended). You can check whether it's installed by open `Control Panel > Programs and Features` and find it in the list.

`virtualenv` can be installed using:

```
pip install virtualenv
```

## How to run?

Make sure you have installed all the required software in **Prerequisites** before proceed.

Simply run the `run.py` script.

> _Note that on the first time the script runs, it will try to create a virtual environment (if not exist) and install all dependencies so make sure you have **internet connection available**_

### On Linux (and probably on MacOS??*)

Open a terminal app and run:

```
python3 run.py
```

OR set the executable permission for the script (you need to do this only ONCE) using:

```
chmod +x run.py
```

AND then use:

```
./run.py
```

to run

### On Windows

Open the Command-line window and run:

```
python run.py
```

## How to build?

Make sure you have installed all the required software in **Prerequisites** before proceed.

> _Note that on the first time the script runs, it will try to create a virtual environment (if not exist) and install all dependencies so make sure you have **internet connection available**_

> _Note: Bukworm is currently use `pyinstaller` to build which the final file size is quite HUGE (100+ MB). I'm trying different ways to bring the build size down and the build tool will sure be changed in the future._

Then run the `build.py` script. The built result will be stored at the `dist` directory.

### On Linux (and probably on MacOS??*)

Open a terminal app and run:

```
python3 build.py
```

OR set the executable permission for the script (you need to do this only ONCE) using:

```
chmod +x build.py
```

AND then use:

```
./build.py
```

to build

### On Windows

Open the Command-line window and run:

```
python build.py
```

## License
_Choosing..._

> \* I have never used MacOS so I have no idea if it worked but I think it should because Python is cross-platform.
