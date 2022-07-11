# This script is meant to run in a virtual environment where
# pyinstaller is installed

import PyInstaller.__main__ as pyi

if __name__ == "__main__":
    pyi.run([
        "scripts/build.spec"
    ])