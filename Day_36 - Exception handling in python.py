# ## Exception handling in Python
# a = input("Enter your number")
# print(f"multiplication table of {a} is: ")

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a) * i}")
# except:
#     print("Invalid Input")

# print("Some imp lines of code")
# print("End of program")

#example
try:
    num = int(input("enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number is not an integer")

except IndexError:
    print("index error")