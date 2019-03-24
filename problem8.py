# Rock paper scissors game

print('''pick one :
                rock
                scissors
                paper''')

while True:
    try:
        game_on  = {'rock': 1, 'scissors': 2, 'paper': 3}
        player_a = str(input("Player_a : "))
        player_b = str(input("Player_b : "))
        a = game_on.get(player_a)
        b = game_on.get(player_b)
        diff = a-b

        if diff in [-1, 2]:
            print("Player a wins")
            if str(input("Do u want to play again yes/no\n")) == 'yes':
                continue
            else:
                print("Game over")
                break

        elif diff in [-2, 1]:
            print("player b wins")
            if str(input("Do u want to play again yes/no\n")) == 'yes':
                continue
            else:
                print("Game over")
                break
        else:
            print("Draw...Continue")
            continue

    except TypeError:
        print("Make sure you type right")