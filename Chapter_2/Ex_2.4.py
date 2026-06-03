# Exercise 2.4
# MD5 OF A FILE

import hashlib

file_name = input("Enter file name: ")

try:
    with open(file_name, 'rb') as file:
        content = file.read()
        md5_hasher = hashlib.md5(content).hexdigest()
        print(f"The MD5 for the given file is\n{md5_hasher}")

except FileNotFoundError:
    print("File not found!")