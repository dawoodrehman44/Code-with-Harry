# # Break and Continue statements

# for i in range(12):
#     if (i == 10):
#         break
#     print("5 x ", i+1, "=", 5 *( i+ 1))

# print("Loop ko chod kar nikal jao")

# Continue statement
# for i in range(12):
#     if (i == 9):
#         print("Leave/Skip this Iteration")
#         continue
#     print("5 x ", i+1, "=", 5 *( i+ 1))

# Imulate do while loop
i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break