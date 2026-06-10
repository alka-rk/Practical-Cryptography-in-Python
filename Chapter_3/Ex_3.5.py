# Exercise 3.5
# ALL NIST KATS

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

with open('ECBGFSbox128.rsp', 'r') as file:
    lines = file.readlines()
    #print(lines)

    count = 0
    pt_ci_text = {}
    for i in range(len(lines)):
        if count <= 6:
            if lines[i].startswith("PLAINTEXT"):
                plaintext = lines[i].split(" ")[2].strip()
                ciphertext = lines[i+1].split(" ")[2].strip()

                pt_ci_text[plaintext] = ciphertext
                count += 1

print(f"Plaintext-Ciphertext Data:\n{pt_ci_text}")

key = bytes.fromhex('0'*32)

aesCipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend)

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

print("\nPlaintext and Ciphertext:\n")

for plaintext in pt_ci_text:
    ciphertext_found = aesEncryptor.update(bytes.fromhex(plaintext))

    if ciphertext_found.hex() == pt_ci_text[plaintext]:
        print(f"{plaintext} : {ciphertext_found.hex()}")
        print('Ciphertext matched.')
        continue
    else:
        print('Ciphertext not matched!')

print("\nCiphertext and Plaintext:\n")

for plaintext in pt_ci_text:
    plaintext_found = aesDecryptor.update(bytes.fromhex(pt_ci_text[plaintext]))

    if plaintext_found.hex() == plaintext:
        print(f"{pt_ci_text[plaintext]} : {plaintext_found.hex()}")
        print('Plaintext matched.')
        continue
    else:
        print('Plaintext not matched!')