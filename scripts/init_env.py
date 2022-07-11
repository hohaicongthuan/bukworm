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
            return "python"
        else:
            return "bukworm_virtualenv\\Scripts\\python.exe"

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
    if (platform.system() == "Linux"):
        if not os.path.exists("bukworm_virtualenv"):
            subprocess.run([py_exe(), "-m", "virtualenv", "bukworm_virtualenv"])
            subprocess.run([pip_exe(1), "install", "-r", "requirements.txt"])

    elif (platform.system() == "Windows"):
        if not os.path.exists("bukworm_virtualenv"):
            subprocess.run([py_exe(), "-m", "virtualenv", "bukworm_virtualenv"])
            subprocess.run([pip_exe(1), "install", "-r", "requirements.txt"])
    