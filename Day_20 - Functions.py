a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

gmean = (a*b)/(a+b)
def calculategmean (a, b):
    return(gmean)
if (a > b):
    print("first number is greater")
else:
    print("second number is greater")

print("Geometric Mean is = ", gmean)
