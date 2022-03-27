import os
from filecmp import cmp

FILEDIR = os.path.dirname(__file__)

jpg = [f for f in os.listdir(FILEDIR)][0]  # Name of .jpg file to be checked
src = f"{FILEDIR}\{jpg}"  # Path of .jpg file to be checked
dst = input("Recovered files in which directory: ")
log = open(f"{FILEDIR}\log.txt", "w")

for f in os.listdir(dst):
    target = f"{dst}\{f}"

    # Writing files that differ from the original to a text file
    if not cmp(target, src):
        log.write(f"{target}\n")

log.close()
