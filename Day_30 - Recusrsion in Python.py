# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial (n-1)

# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

# Quick Qiz: Write a program to print the Fibonacci Sequence
def febseq (f):
    if (f == 0):
        return 0
    elif (f == 1):
        return 1
    #elif (f == 2):
     #   return (febseq * (1) + febseq * (2))
    else:
        return (febseq(f-1) + febseq(f-2))
print(febseq(6))