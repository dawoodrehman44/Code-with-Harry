# Create a program capable of displaying questions to the use like KBC
# Use list data type to store the questions and their correct answer.
# Display the final amount the person is taking home after playing the game.

name = input("What is your name? ")
print("\nWelcome to the KBC Game!!!!", name, "\nLets start the game")

print("Here is your first Question")

questions = ["1. Where is the capital of Pakistan locaed?","2. Who is the prime minister of Pakistan?", "3. Who is the captain of Pakistan Cricket Team?"]
answers = ["Isb", "SS", "BA"]

a = [100000, 10000000, 100000000]
i = 0

while (i < 3):
    answers1 = input(questions[i])
    if answers1 == answers[i]:
        print("Correct Answer. You have won", a[i], "PKR\n")
    else:
        if i == 0:
            print("Wwrong answer, you are exiting the game with : 0 PKR")
        else:
            print("Wrong answer, you are out with : ", a[i-1], "PKR")
        break
    i = i+1
    if i == 3:
        print("WOOAAAHHH!!!! Mr.", name, "You have completed the game")