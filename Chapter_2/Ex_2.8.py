# Exercise 2.8
# MORE HASH, MORE TIME

import hashlib
import string
import random
import time
import os

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

characters = string.ascii_letters + '0123456789'

pass_length = int(input("Enter the length of the password: "))

def generate(inputset, max_length):

    if max_length <= 0:
        return
    
    for c in inputset:
        yield c
    for c in inputset:
        for next in generate(inputset, max_length - 1):
            yield c + next

input_set = list(generate(characters, pass_length))

l = len(input_set)
print(f"Total number of symbols in input set: {l}\n")

print("Using SHA-1:\n")

cal_time = []

for i in range(10):

    preimage = random.choice(input_set)
    test_hash = hashlib.sha1(preimage.encode()).hexdigest()

    start = time.perf_counter()

    for char in input_set:
        hash = hashlib.sha1(char.encode()).hexdigest()

        if hash == test_hash:
            break

    end = time.perf_counter()

    time_taken = end - start
    cal_time.append(time_taken)

    print(f"Preimage seed: {preimage}, Time taken: {time_taken:.8f} seconds")

average = sum(cal_time) / len(cal_time)
print(f"Average time: {average:.8f}")

print("\nUsing SHA-256:\n") 

cal_time = []

for i in range(10):

    preimage = random.choice(input_set)
    test_hash = hashlib.sha256(preimage.encode()).hexdigest()

    start = time.perf_counter()

    for char in input_set:
        hash = hashlib.sha256(char.encode()).hexdigest()

        if hash == test_hash:
            break

    end = time.perf_counter()

    time_taken = end - start
    cal_time.append(time_taken)

    print(f"Preimage seed: {preimage}, Time taken: {time_taken:.8f} seconds")

average = sum(cal_time) / len(cal_time)
print(f"Average time: {average:.8f}")

print("\nUsing Scrypt:\n") #It takes longer time than above two

cal_time = []
for i in range(3):

    preimage = random.choice(input_set).encode()
    #test_hash = hashlib.sha1(preimage.encode()).hexdigest()

    start = time.perf_counter()

    #salt = os.urandom(16)
    salt = b'123'
    print(f"Salt: {salt.decode()}")

    kdf = Scrypt(salt=salt, length=32,
                n=2**14, r=8, p=1,
                backend=default_backend())

    key = kdf.derive(preimage)

    for text in input_set:

        kdf = Scrypt(salt=salt, length=32,
                n=2**14, r=8, p=1,
                backend=default_backend())
        
        enc = text.encode()
        candidate_key = kdf.derive(enc)

        if candidate_key == key:
            password = text
            break

    end = time.perf_counter()

    time_taken = end - start
    cal_time.append(time_taken)

    print(f"Preimage seed: {salt.decode()+password}, Time taken: {time_taken:.8f} seconds")

average = sum(cal_time) / len(cal_time)
print(f"Average time: {average:.8f}")
