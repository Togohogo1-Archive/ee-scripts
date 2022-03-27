import os
from datetime import datetime
from shutil import copy

FILEDIR = os.path.dirname(__file__)

file = [f for f in os.listdir(FILEDIR)][0]  # Name of file to be copied
_, ext = os.path.splitext(file)
src = f"{FILEDIR}\{file}"  # Absolute path of file to be copied
dst = input("Copy to which directory: ")
stamp = str(datetime.utcnow()).replace(":", "_").replace(" ", ",")

dupes = int(input("How many copies: "))

for i in range(dupes):
    # Incremental naming with timestamps
    new = f"{FILEDIR}\{i},{stamp}{ext}"

    # Renaming original .jpg file and make copies of it
    os.rename(src, new)
    src = new

    copy(src, dst)
