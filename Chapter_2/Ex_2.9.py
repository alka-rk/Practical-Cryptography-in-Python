# Exercise 2.9
# PROOF OF WORK

import hashlib

target = 2**254

nonce = 0
message = 'Cryptography'

while True:

    test_message = message + str(nonce)
    hash = hashlib.sha256(test_message.encode()).hexdigest()
    int_hash = int(hash, 16)

    if int_hash < target:
        print(f"Target found with nonce {nonce} and message: {test_message}")
        break

    nonce +=1