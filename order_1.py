import random
def get_number():
    """Taked player number and checked it is number"""
    while True:
        try:
            get_number = int(input("Guess the number:"))
            break
        except ValueError:
            print("It's not e number")
    return get_number
def guess_number():
    """Main function of our game"""
    guess_number = random. randint(1, 100)
    player_number = get_number()
    while guess_number != player_number:
        if guess_number >= player_number:
            print("Too small")
        else:
            print("Too big")
        player_number = get_number()
    print("You win")


print(guess_number())




