import os
import re
import time

# pip install send2trash
from send2trash import send2trash

regex = r"^[0-9]+,[0-9]{4}-[0-9]{2}-[0-9]{2},[0-9]{2}_[0-9]{2}_[0-9]{2}.[0-9]{6}.jpg$"

dst = input("Delete files in which directory: ")
choice = int(input("[0] Recycle bin\n[1] Shift delete\n"))

start_time = time.time()

for f in os.listdir(dst):
    if re.match(regex, f):
        if choice:
            os.remove(f"{dst}\{f}")  # Permanent deletion
        else:
            send2trash(f"{dst}\{f}")  # Manually emptying trash

print(f"{time.time()-start_time} seconds")
