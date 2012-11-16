LastVK
====================
Download track that plays on LastFM

Works on MacOS/Windows/Linux

## Installation from source :

- download and install [PyQt4](http://www.riverbankcomputing.co.uk/software/pyqt/download)
- `pip install -r requirements.txt`
- run `python LastVK.py`

**NOTE:** on Windows platform install packages to python install path (e.g. `C:\Python27`)

## Bundling :
- download and unpack [pyinstaller](http://www.pyinstaller.org/)
- `export PATH=$PATH:/path/to/pyinstaller`
- `pyinstaller.py LastVK.spec`
- open ./dist dir to see bundle