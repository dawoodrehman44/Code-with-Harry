# Reading_a_file
# f = open("myfile.txt", "r") # r = read
# text = f.read()
# print(text)
# f.close()

# # Writing_a_file
# z = open("myfile.txt", "w")
# z.write("hello world")
# z.close()

## using wiht statement
with open("myfile.txt", "a") as f:
    f.write("Hey i am inside with")