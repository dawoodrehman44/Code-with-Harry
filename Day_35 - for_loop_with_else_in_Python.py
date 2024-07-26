# for loop with else
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("out of loop")

print("")
## while loop with else
i = 0
while i <7:
    print(i)
    i = i + 1
    if i == 4:
        break
else:
    print("out of loop")
#################################################

## Without break function
# for loop with else
for i in range(6):
    print(i)
    # if i == 4:
    #     break
else:
    print("out of loop")

print("")
## while loop with else
i = 0
while i <7:
    print(i)
    i = i + 1
    # if i == 4:
    #     break
else:
    print("out of loop")

#########################################################
for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("out of loop")