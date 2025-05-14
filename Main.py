# 1. Import the random module.
import random

print("Welcome to our little game of Rock Paper Scissors lil bro!")
print()

play_again = True
while play_again:
        
    # 2. Generate a random number between 1 and 3 and set it equal to a variable called computer (hint: use the randint() function) 

    computer = random.randint(1,3)


    # 3. Using input, get the user's choice where 1 is rock, 2, paper, and 3 is scissors. Store the user's input in a variable called user.

    choice = int(input("choose one \n (1) for Rock \n (2) for Paper \n (3) for Scissors: "))

    # 4. Use if-statements to determine the winner of the game and print the result
    # paper beats rock
    # rock beats scissors 
    # scissors beats paper
    # If the computer and the user choose the same option, print "It's a tie!". If the computer wins, print "Computer wins!". If the user wins, print "You win!". 

    print("Computer chose", computer)

    print(computer == choice)

    if computer == choice:
        print("lil bro. We tied 😐")
    elif computer == 2 and choice == 1:
        print("You lose lil bro! 😂")
    elif computer == 1 and choice == 3:
        print("You lose lil bro! 😂")
    elif computer == 3 and choice == 2:
        print("You lose lil bro! 😂")
    elif choice > 3 or choice < 1:
        print("lil you have to choose one of the 3 numbers! 😡😡😡")
    else:
        print("you win lil bro 😡")


    # making the loop



    user_input = input("You want to play again lil bro? (yes/no): ").lower
    if user_input == "no":
        play_again = False

        print("Thanks for playing with me lil bro 😊")