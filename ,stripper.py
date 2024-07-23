#!/usr/bin/env python3
from pathlib import Path
from sys import argv
import subprocess


def get_file_extensions(path, ext):
    search_path = Path(path)
    FIND_CMD = f"fd . '{search_path}' -t f -e {ext}"
    GREP_CMD = r"grep -Eo '\.[^./]*$' | sort -u"
    print(f"Find command: {FIND_CMD}")
    find_process = subprocess.getoutput(FIND_CMD + ' | ' + GREP_CMD)
    return find_process


if __name__ == "__main__":
    print(argv[1], argv[2])
    get_file_extensions(argv[1], argv[2])
