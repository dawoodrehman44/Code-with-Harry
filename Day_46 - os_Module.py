## to make directory for a course or a project.
# for example i am making a folder for 100 days of python course,
# and after that i am making a seperate folder for each day.

import os

# if(not os.path.exists("data")):
#      os.mkdir("data")

# for i in range(0, 100):
#     os.mkdir(f"data/day{i+1}")

# # # lets say, you want to rename the names of folder 1 to 100
# for i in range (0, 100):
#     os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")

# lets you want to find thu number of folders in your folder
folders = os.listdir("data")
print(os.getcwd())

# for folders in folders:
#     print(folders)
##############################################################
# now you want to explore further the number of folder details

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))
###############################################################
# to look off for the directory
# folders = os.listdir("data")
# print(os.getcwd())
##############################################################
# to remove a folder
os.remove()

# to remove a directory
os.removedirs()