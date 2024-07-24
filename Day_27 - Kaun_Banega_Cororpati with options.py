name = input("What is your name? ")
print("\nWelcome to the KBC Game!!!!", name, "\nLet's start the game")

print("Here is your first question:")

questions = [
    "1. Where is the capital of Pakistan located?",
    "2. Who is the prime minister of Pakistan?",
    "3. Who is the captain of the Pakistan Cricket Team?"
]
answers = ["Isb", "SS", "BA"]
options = [
    ["A. Isb", "B. Lhr", "C. Khi", "D. Pesh"],
    ["A. IK", "B. SS", "C. AAZ"],
    ["A. BA", "B. SA", "C. FZ"]
]

prizes = [50, 100, 200]
i = 0

while i < len(questions):
    print(questions[i])
    for option in options[i]:
        print(option)
    
    answer = input("Please enter the correct option: ").strip().upper()
    
    # Map user's answer to corresponding answer in the answers list
    if answer == 'A':
        selected_answer = options[i][0][3:]
    elif answer == 'B':
        selected_answer = options[i][1][3:]
    elif answer == 'C':
        selected_answer = options[i][2][3:]
    elif answer == 'D' and len(options[i]) == 4:
        selected_answer = options[i][3][3:]
    else:
        print("Invalid option. Exiting the game.")
        break
    
    if selected_answer == answers[i]:
        print("Correct Answer. You have won", prizes[i], "PKR\n")
    else:
        if i == 0:
            print("Wrong answer, you are exiting the game with: 0 PKR")
        else:
            print("Wrong answer, you are out with:", prizes[i-1], "PKR")
        break
    
    i += 1
    
    if i == len(questions):
        print("WOOAAAHHH!!!! Mr./Ms.", name, "You have completed the game")
        print("You are taking home:", sum(prizes), "PKR")
