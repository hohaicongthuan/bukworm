"""
Check, initialise virtual environment (if not exist) and install dependencies in requirements.txt
"""

import os
import platform
import subprocess

def py_exe(path=False):
    if (platform.system() == "Linux"):
        if path:
            return "bukworm_virtualenv/bin/python3"
        else:
            return "python3"
    elif (platform.system() == "Windows"):
        if path:
            return "bukworm_virtualenv\\Scripts\\python.exe"
        else:
            return "python"

def pip_exe(path=False):
    if (platform.system() == "Linux"):
        if path:
            return "bukworm_virtualenv/bin/pip3"
        else:
            return "pip3"
    elif (platform.system() == "Windows"):
        if path:
            return "bukworm_virtualenv\\Scripts\\pip.exe"
        else:
            return "pip"

def init_env():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        pkg_list = f.read().splitlines()

    if (platform.system() == "Linux"):
        if not os.path.exists("bukworm_virtualenv"):
            subprocess.run([py_exe(), "-m", "virtualenv", "bukworm_virtualenv"])
            for pkg in pkg_list:
                subprocess.run(" ".join([pip_exe(1), "install", pkg]))

    elif (platform.system() == "Windows"):
        if not os.path.exists("bukworm_virtualenv"):
            subprocess.run([py_exe(), "-m", "virtualenv", "bukworm_virtualenv"])
            for pkg in pkg_list:
                subprocess.run(" ".join([pip_exe(1), "install", pkg]))
