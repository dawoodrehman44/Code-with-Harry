
marks = [0,1,5, "Harry", 2, 18, True]

print(marks)
print(marks[1:8])
print(marks[1:8:2])

# List Comprehension
lst = [i for i in range(11)]
print(lst)

# or i can write
lst = [i*i for i in range(10)]
print(lst)

# or i can write
lst = [i*i for i in range(10) if i%2 == 0]
print(lst)

# Example: Printing elements within a particular range
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes

# Example: Printing elements from a given index till the end
animals = ["cat", "dog", "bat", "mouse", "pig", 
           "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes

# Example: Printing all elements from start to a given index
animals = ["cat", "dog", "bat", "mouse", "pig", 
           "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes

# Example: Printig alternative values
animals = ["cat", "dog", "bat", "mouse", 
           "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2]) # using positive indexes
print(animals[-8:-1:2]) # using negative indexes

# Example: Printing every 3rd consecutive value within a given range
animals = ["cat", "dog", "bat", "mouse", 
           "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])
