marks = [12, 56, 32, 98, 12, 45, 1, 4]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Harry, awesome")
#     index += 1

# Now lets use Enumerate function
for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 3):
        print("Harry, awesome")

# another example
fruits = ["apple", "banana", "mango"]
for index, fruits in enumerate(fruits):
    print(index, fruits)