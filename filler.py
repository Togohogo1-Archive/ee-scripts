import os

path = input("File path: ")

curr_bytes = os.path.getsize(path)
print("Current bytes:", curr_bytes)

new_bytes = int(input("Desired bytes: "))
diff = new_bytes - curr_bytes

with open(path, "ab") as f:
    for i in range(diff):
        f.write(b"\0")

    f.close()
