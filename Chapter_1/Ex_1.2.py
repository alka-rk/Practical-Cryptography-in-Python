# Exercises 1.2
# AUTOMATED DECODING 

import string
from nltk.corpus import words

#for cipher texts having spaces
file_name = input("Enter the file name: ")
n = int(input("Enter the size of shift: "))

try:
    with open(file_name, "r") as file:

        content = file.read()
        clean_text = ""
        for char in content:
            if char.isalpha() or char.isspace():
                clean_text += char
        upp = clean_text.upper()
        #print(upp)

        def encode(plain_text,shift):
            cipher_f = ""
            for char in plain_text:
                if char.isalpha():
                    ascii_value = ord(char)
                    k = string.ascii_uppercase[(ascii_value - 13 + shift) % 26]
                    cipher_f += k
                else:
                    cipher_f += char
            return cipher_f
        print(f"The cipher text:\n\n {encode(upp,n)}")

        #Decode using English dictionary
        english_words = set(words.words())

        def decode(ci_text,sh):
            decode_f = ""
            for char in ci_text:
                if char.isalpha():
                    ascii_value = ord(char)
                    k = string.ascii_uppercase[(ascii_value - 13 - sh) % 26]
                    decode_f += k
                else:
                    decode_f += char
            return decode_f
        
        #print(decode(encode(upp,1), 1)), To check if the decode() works
        
        def score_test(text):
            count = 0
            ciph = text
            split_text = ciph.lower().split() #Without lower() it doesn't work

            for char in split_text:
                if char in english_words:
                    count += 1

            return count
        
        best_score = 0
        best_shift = 0
        best_text = ""

        for i in range(26):
            decoded = decode(encode(upp,n),i)
            score = score_test(decoded)

            print(f"Shift {i} : \n\n{decoded}")

            if score > best_score:
                best_score = score
                best_shift = i
                best_text = decoded

        print(f"\nMost likely shift is {best_shift} and decoding is :\n\n {best_text} ")

except FileNotFoundError:
    print("File not FOUND!")


#for cipher texts having no spaces
file_name = input("Enter the file name: ")
n = int(input("Enter the size of shift: "))

try:
    with open(file_name, "r") as file:

        content = file.read()
        clean_text = ""
        for char in content:
            if char.isalpha():
                clean_text += char
        upp = clean_text.upper()
        #print(upp)

        def encode(plain_text,shift):
            cipher_f = ""
            for char in plain_text:
                ascii_value = ord(char)
                k = string.ascii_uppercase[(ascii_value - 13 + shift) % 26]
                cipher_f += k
                
            return cipher_f
        print(f"The cipher text:\n\n{encode(upp,n)}")

        #Decode using English dictionary
        english_words = set(words.words())

        def decode(ci_text,sh):
            decode_f = ""
            for char in ci_text:
                ascii_value = ord(char)
                k = string.ascii_uppercase[(ascii_value - 13 - sh) % 26]
                decode_f += k
                
            return decode_f
        
        #print(decode(encode(upp,1), 1)) #To check if the decode() works
        
        def score_test(text):
            count = 0
            ciph_text = text.lower()

            for word in english_words:
                #Ignore tiny words
                if (len(word)>2) and word in ciph_text:
                    count += 1

            return count
        
        best_score = 0
        best_shift = 0
        best_text = ""

        for i in range(26):
            decoded = decode(encode(upp,n),i)
            score = score_test(decoded)

            print(f"Shift {i} : \n\n{decoded}")
            print(f"Dictionary matches : {score}\n")

            if score > best_score:
                best_score = score
                best_shift = i
                best_text = decoded

        print(f"\nMost likely shift is {best_shift} and decoding is :\n\n{best_text} ")

except FileNotFoundError:
    print("File not FOUND!")
