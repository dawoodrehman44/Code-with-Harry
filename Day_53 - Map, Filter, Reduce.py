# # def cube(x):
# #     return x * x * x

# # print(cube(2))

# l = [1, 2, 4, 6, 4, 3]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))
# # print(newl)

# # we can short the code with the help of map() function

# # newl = list(map(cube, l))
# # print(newl)

# # FILTER
# def filter_func(a):
#     return a > 2

# newnewl = list(filter(filter_func, l))
# print(newnewl)


### REDUCE
from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: x + y, numbers)

# print the sum
print(sum)