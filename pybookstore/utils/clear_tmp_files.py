#!/usr/bin/env python3
from pybookstore import basedir
import re
import os


PATTERNS = (
    '^flymd\..+$',  # markdown preview
    '^.+\..+~$',    # tmp files like 'file.py~'
    '__pycache__',  # cache files
)


def clear_all():
    for root, dirs, files in os.walk(basedir):
        for filename in files:
            if re.match()
    
