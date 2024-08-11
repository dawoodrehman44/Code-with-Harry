# # Example
# def double(x):
#     return x * 2
# print(double(5))

double = lambda x : x*2
print(double(5))

# lambda function can multiple arguments too
avg = lambda x, y: (x + y)/2
print(avg(3, 5))

# we use Lambda for one liner functions 
# and when we pass butil-in functions
# they are often used to higher order functions such as map, filter, and reduce.
# used when a small fucntions is required for a short period of time.