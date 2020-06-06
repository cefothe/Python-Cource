import random
computer_guess= random.randint(1,100)
player_guess = (int(input("Whats your guess")))
while player_guess != computer_guess:
    player_guess = (int(input("Whats your guess")))
    if player_guess == computer_guess:
        print("Correct!")
    elif player_guess<computer_guess:
        print("too low")
    else:
        print("too high")