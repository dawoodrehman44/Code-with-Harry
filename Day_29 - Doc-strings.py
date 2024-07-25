# Doc strings, we write below the name of the function 
# or above the body of the function
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)
