# # Four types of Arguments
# # 1 : Default Arguments
def average(a=9, b= 1):
    print("The average is ", (a+b)/2)
average(4, 6)
# or
average(5)
#or
average(b=9)

# # 2 : Keyword Arguments
# ## you can change the arguments
# ### For example using the above function in different order
average(b=3, a=1)

# # 3 : Variable Length arguments
def average (*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers: 
        sum = sum + i
    print("Average is: ", sum/len(numbers))

# average(5, 11, 13, 11, 10)

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchaman", lname = "Barness", fname = "Dawood")

# 4 : Required Arguments
# using return function
def average (*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers) 
c = average(1, 4, 12, 100)
print("The average is: ", c)


