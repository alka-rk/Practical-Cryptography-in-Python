# Exercise 2.6
# THE POWER OF ONE, BUT BIGGER!

import hashlib
import string
import random
import time

print("1. Input set is lowercase and uppercase letters.\n")

alphabet = string.ascii_letters
l = len(alphabet)
print(f"Total number of symbols in input set: {l}\n")

cal_time = []

for i in range(10):

    preimage = random.choice(alphabet)
    test_hash = hashlib.md5(preimage.encode()).hexdigest()

    start = time.perf_counter()

    for char in alphabet:
        hash = hashlib.md5(char.encode()).hexdigest()

        if hash == test_hash:
            break

    end = time.perf_counter()

    time_taken = end - start
    cal_time.append(time_taken)

    print(f"Preimage seed: {preimage}, Time taken: {time_taken:.8f} seconds")

average = sum(cal_time) / len(cal_time)
print(f"Average time: {average:.8f}")


print("\n2. Input set is lowercase letters, uppercase letters and numbers.\n")

set = string.ascii_letters + '0123456789'
l = len(set)
print(f"Total number of symbols in input set: {l}\n")

cal_time = []

for i in range(10):

    preimage = random.choice(set)
    test_hash = hashlib.md5(preimage.encode()).hexdigest()

    start = time.perf_counter()

    for char in set:
        hash = hashlib.md5(char.encode()).hexdigest()

        if hash == test_hash:
            break

    end = time.perf_counter()

    time_taken = end - start
    cal_time.append(time_taken)

    print(f"Preimage seed: {preimage}, Time taken: {time_taken:.8f} seconds")

average = sum(cal_time) / len(cal_time)
print(f"Average time: {average:.8f}")


print("\n3. Input set is all printable characters.\n")

set = string.printable
l = len(set)
print(f"Total number of symbols in input set: {l}\n")

cal_time = []

for i in range(10):

    preimage = random.choice(set)
    test_hash = hashlib.md5(preimage.encode()).hexdigest()

    start = time.perf_counter()

    for char in set:
        hash = hashlib.md5(char.encode()).hexdigest()

        if hash == test_hash:
            break

    end = time.perf_counter()

    time_taken = end - start
    cal_time.append(time_taken)

    print(f"Preimage seed: {preimage}, Time taken: {time_taken:.8f} seconds")

average = sum(cal_time) / len(cal_time)
print(f"Average time: {average:.8f}")