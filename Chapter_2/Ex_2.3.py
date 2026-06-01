# Exercise 2.3
# OBSERVING AVALANCHE

import hashlib

#Enter the messages to be hashed
message_1 = input("Enter the message 1: ")
message_2 = input("Enter the message 2: ")

m_list = [message_1, message_2]

hash_list = []
for text in m_list:
    b_text = text.encode()
    md5hasher = hashlib.md5(b_text).hexdigest()
    hash_list.append(md5hasher)

binary_string = []
for hexstring in hash_list:
    binstring = format(int(hexstring, 16), '0128b')
    binary_string.append(binstring)

count = 0
bin_list = []
for b in binary_string:
    lst = list(b)
    bin_list.append(b)

for i in range(128):
    if bin_list[0][i] != bin_list[1][i]:
        count += 1

print(f"The number of bit changes is {count}.")