# guessing game

import random
number = random.randint(1, 9)
user_number = 0
count = 0

while True:

    user_number = int(input("enter a number\n"))

    if user_number == "exit":
        break

    user_number = int(user_number)
    count += 1
    print("random number is", number)

    if user_number > number:
        print("Too high ")
        if str(input("play again yes/no\n")) == 'yes':
            continue

        else:
            print("Game end")
            exit()

    elif user_number < number:
        print("too low")
        if str(input("play again yes/no\n")) == 'yes':
            continue
        else:
            print("game end")
            exit()
    else:
        print("level")
        exit()

