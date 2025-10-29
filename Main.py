import random
import os
import time

clear = os.system('cls||clear')

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

print("🎮 Welcome to our little game of Rock Paper Scissors lil bro! 🎮")
print("Let's see if you can beat me 😏\n")

play_again = True
win_streak = 0  # win streak counter
lose_streak = 0  # lose streak counter
tie_streak = 0   # tie streak counter
round_num = 1

while play_again:
    print(f"\n--- Round {round_num} ---")
    print(f"🔥 Win streak: {win_streak} | 💀 Lose streak: {lose_streak} | 🤝 Tie streak: {tie_streak}")
    time.sleep(0.5)

    # If player lost 3 times, force a win
    if lose_streak >= 3:
        print("😢 You lost 3 times in a row! I'll let you win this one, lil bro.")
        choice = input("Choose one \n (1) for Rock \n (2) for Paper \n (3) for Scissors: ")
        if not choice.isdigit():
            print("lil bro you gotta type a NUMBER 😡 (maybe 1, 2, or 3?)")
            continue
        choice = int(choice)
        if choice < 1 or choice > 3:
            print("lil bro you have to choose one of the 3 numbers! 😡😡😡")
            continue
        # Computer picks what loses to player's choice
        if choice == 1:
            computer = 3  # scissors
        elif choice == 2:
            computer = 1  # rock
        else:
            computer = 2  # paper
        print(f"Computer chose {choices[computer]} 🖥️")
        win_streak += 1
        lose_streak = 0
        tie_streak = 0
        if win_streak == 1:
            print("🎉 You win lil bro 😡")
        elif win_streak == 2:
            print("🔥 You win again lil bro! Win streak: 2")
        elif win_streak >= 3:
            print(f"🔥 You on fire lil bro! Win streak: {win_streak}")
    else:
        computer = random.randint(1, 3)
        choice = input("Choose one \n (1) for Rock \n (2) for Paper \n (3) for Scissors: ")
        if not choice.isdigit():
            print("lil bro you gotta type a NUMBER 😡 (maybe 1, 2, or 3?)")
            continue
        choice = int(choice)
        if choice < 1 or choice > 3:
            print("lil bro you have to choose one of the 3 numbers! 😡😡😡")
            continue
        print("Rock...")
        time.sleep(0.5)
        print("Paper...")
        time.sleep(0.5)
        print("Scissors...")
        time.sleep(0.5)
        print(f"Computer chose {choices[computer]} 🖥️")
        if computer == choice:
            print("😐 It's a tie lil bro.")
            win_streak = 0
            lose_streak = 0
            tie_streak += 1
            if tie_streak > 1:
                print(f"🤝 That's {tie_streak} ties in a row!")
        elif (computer == 2 and choice == 1) or (computer == 1 and choice == 3) or (computer == 3 and choice == 2):
            print("😂 You lose lil bro!")
            win_streak = 0
            lose_streak += 1
            tie_streak = 0
        else:
            win_streak += 1
            lose_streak = 0
            tie_streak = 0
            if win_streak == 1:
                print("🎉 You win lil bro 😡")
            elif win_streak == 2:
                print("🔥 You win again lil bro! Win streak: 2")
            elif win_streak >= 3:
                print(f"🔥 You on fire lil bro! Win streak: {win_streak}")

    round_num += 1

    # Ask to play again
    while True:
        user_input = input("You want to play again lil bro? (y/n): ").strip().lower()
        if user_input in ("y", "n"):
            break
        print("lil bro you gotta type 'y' or 'n' 😡")

    if user_input == "n":
        print("\n👋 Thanks for playing with me lil bro 😊")
        print(f"Final win streak: {win_streak} | Final lose streak: {lose_streak} | Final tie streak: {tie_streak}")
        break