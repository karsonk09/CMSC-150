import random
done = False

level_1 = 50
level_2 = 100
level_3 = 200
level_4 = 400
level_5 = 800
level_6 = 1600


def quit():
    while not done:
        quit = input("Do you want to quit? ")
        if quit == "y":
            done = True
        start_game()


def start_game():
    attack = input("Do you want to attack the troll? ")
    if attack == "y":
        exp = random.randrange(45, 100)
        print("You killed a troll, you gained", exp, "experience!")
        if exp >= level_1:
            print("You are now level 1!")
        elif exp >= level_2:
            print("You are now level 2!")


def start_screen():
    print("""Welcome to Dragons and Trolls!""")
    start = input("Would you like to start a new game? ")
    if start == "y":
        start_game()
    else:
        quit()





start_screen()







