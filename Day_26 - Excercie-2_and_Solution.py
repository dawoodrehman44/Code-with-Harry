import time
t = int(time.strftime("%H"))

if (t >= 4 and t <= 11):
    print("Good Morning")
elif(t >= 12 and t <= 17):
    print("Goof Afternoon")
elif(t >= 18 and t <= 22):
    print("Good Evening")
else:
    print("Good Night")