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

random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(3))
print("WELCOME to the secret services game!!")
language = input("Enter your language word ")
program = input("You want to perform coding or decoding: ")
if program == "coding":
    def coding():
        if len(language) < 3:
            a = language[1:]
            b = a + language[0]
            c = b + random_chars
            del a
            print(c)
        else:
            cd =language[::-1]
            print(cd)
    coding()

else:
    def decoding():
        if len(language) < 3:
            print(language[::-1])
        else:
            d = language[0:3]
            e = d[0:2]
            f = d[-1]
            g = f + e
            print(g)
    decoding()
