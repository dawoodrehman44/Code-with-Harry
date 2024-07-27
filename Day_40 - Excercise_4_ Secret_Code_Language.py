# write a python program to translate a message into secret code language. Use the rules to translate normal english into secret code language.

# Coding
# if the word contains atleast three characters, remove the first letter and append it at the end
#    now append three random characters at the starting and the end.
# else:
#   simply reverse the string 

# Decoding
# if the word contains less than 3 characters, reverse it.
# else:
#   remove 3 random characters from the end.Now remove the last letter and  append it to the begining

# your program should ask whether you want to code or decode 

import numpy as np
import random
import string

language = input("Enter your language word ")
random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(3))
#print(random_chars)

def coding():
    if len(language) < 3:
        a = language[1:]
        b = a + language[0]
        c = b + random_chars
        del a
        return(c)
    else:
        return(language[::-1])
print(coding())

# # Now lets decode the coding
# # # Decoding
# def decoding():
#     if len(language) <= 3:
#         print(language[::-1])
#     else:
#         d = language[2:]
#         del d
#         e = language[-3]
#         f = e + language
#         return(f)
# print(decoding())

# Now lets decode the coding
# # Decoding
# def decoding():
#     ab = str(coding)
#     if len(ab) < 3:
#         return(ab[::-1])
#     else:
#         d = ab[2:]
#         del d
#         e = ab[-3]
#         f = e + ab
#         return(f)
# print(decoding())

ab = str(coding)
if len(ab) < 3:
    print(ab[::-1])
else:
    d = ab[2:]
    del d
    e = ab[-3]
    f = e + ab
    print(f)
# else:
#   remove 3 random characters from the end.Now remove the last letter and  append it to the begining