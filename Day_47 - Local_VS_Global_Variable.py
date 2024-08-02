# x = 4
# print(x)

# def hello():
#     x = 5
#     print(f"The local x is {x}")
#     print("Hello harry")

# print(f"The global x is {x}")
# hello()
# print(f"The global x is {x}")

x = 10 #global variable

def my_function():
    global x
    x = 4           #the value of local x has been changed now due to global function and it now becomes a global x
    y = 5 #local variable
    print(y)
my_function()

print(x)