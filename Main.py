import random

print("Welcome to our little game of Rock Paper Scissors lil bro!")
print()

play_again = True
win_streak = 0  # win streak counter

while play_again:
  
    computer = random.randint(1, 3)

    choice = int(input("choose one \n (1) for Rock \n (2) for Paper \n (3) for Scissors: "))

    print("Computer chose", computer)

    if choice < 1 or choice > 3:
        print("lil you have to choose one of the 3 numbers! 😡😡😡")
        continue
   
    if computer == choice:
        print("lil bro. We tied 😐")
        win_streak = 0
    elif (computer == 2 and choice == 1) or (computer == 1 and choice == 3) or (computer == 3 and choice == 2):
        print("You lose lil bro! 😂")
        win_streak = 0
    else:
        win_streak += 1
        if win_streak == 1:
            print("you win lil bro 😡")
        elif win_streak == 2:
            print("you win again lil bro 🔥 win streak: 2")
        elif win_streak >= 3:
            print("you on fire lil bro 🔥 win streak: 3")

    # Ask to play again
    user_input = input("You want to play again lil bro? (yes/no): ").lower()
    if user_input == "no":
        play_again = False
        print("Thanks for playing with me lil bro 😊")