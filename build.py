#! /usr/bin/env python3
# Automation script for lazy people

"""
Check, initialise virtual environment (if not exist) and install dependencies in requirements.txt
Run build command
"""

import platform
import subprocess

from scripts import init_env


if __name__ == "__main__":
    
    init_env.init_env()

    if (platform.system() == "Linux"):
        subprocess.run([init_env.py_exe(1), "scripts/build_from_virtualenv.py"])

    elif (platform.system() == "Windows"):
        subprocess.run([init_env.py_exe(1), "scripts\\build_from_virtualenv.py"])
    
    