# Exercise 2.7
# PASSWORD LENGTH’S EFFECTS ON ATTACK TIME

import hashlib
import string
import random
import time

characters = string.printable

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

cal_time = []

for i in range(10):

    preimage = random.choice(input_set)
    test_hash = hashlib.md5(preimage.encode()).hexdigest()

    start = time.perf_counter()

    for char in input_set:
        hash = hashlib.md5(char.encode()).hexdigest()

        if hash == test_hash:
            break

    end = time.perf_counter()

    time_taken = end - start
    cal_time.append(time_taken)

    print(f"Preimage seed: {preimage}, Time taken: {time_taken:.8f} seconds")

    #to see preimage seed as bit-string
    #print(f"Preimage seed: {preimage.encode()}, Time taken: {time_taken:.8f} seconds")

average = sum(cal_time) / len(cal_time)
print(f"Average time: {average:.8f}")