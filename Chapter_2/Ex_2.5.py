# Exercise 2.5
# THE POWER OF ONE

import hashlib
import string
import random
import time

cal_time = []

for i in range(10):

    preimage = random.choice(string.ascii_lowercase)
    test_hash = hashlib.md5(preimage.encode()).hexdigest()

    start = time.perf_counter()

    for char in string.ascii_lowercase:
        hash = hashlib.md5(char.encode()).hexdigest()

        if hash == test_hash:
            break

    end = time.perf_counter()

    time_taken = end - start
    cal_time.append(time_taken)

    print(f"Preimage seed: {preimage}, Time taken: {time_taken:.8f} seconds")

average = sum(cal_time) / len(cal_time)
print(f"Average time: {average:.8f}")