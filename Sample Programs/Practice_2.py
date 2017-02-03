import random
done = False

global exp

level_1 = 50
level_2 = 100
level_3 = 200
level_4 = 400
level_5 = 800
level_6 = 1600
attack = 0
defense = 0
armor = 0
magic = 0

# Level up if statements
def lvl_up():
    attack = 0
    defense = 0
    magic = 0
    if level_1 <= exp < level_2:
        print("You are now level 1!")
        x = random.randrange(1, 4)
        y = attack + x
        z = defense + x
        m = magic + x
        print("Stats increase!")
        print("Attack: 0 +", x, ">>>", y)
        attack += x
        print("Defense: 0 +", x, ">>>", z)
        defense += x
        print("Magic: 0 +", x, ">>>", m)
    elif level_2 <= exp < level_3:
        print("You are now level 2!")
        x = random.randrange(1, 4)
        y = attack + x
        z = defense + x
        m = magic + x
        print("Stats increase!")
        print("Attack: ", attack, "+", x, ">>>", y)
        attack += x
        print("Defense: ", defense, "+", x, ">>>", z)
        defense += x
        print("Magic: ", magic, "+", x, ">>>", m)
    elif level_3 <= exp < level_4:
        print("You are now level 3!")

def main():
    start_screen()


def quit():
    while not done:
        quit = input("Do you want to quit? ")
        if quit == "y":
            done = True
        start_game()


def start_game():
    mother_relationship = 0
    print()
    print("""Hello adventurer! Welcome to the world of Avendale, where citizens thrive off of
    their livestock and their rivers. Where mountainous peaks rise to touch the highest clouds
    and where the sea reaches down to the most cavernous depths of the Earth's core.""")
    print()
    name = input("What is your name, adventurer? ")
    print()
    print("Hello,", name,", son of Elisia, Queen of all the realm, and welcome to Avendale!")
    print()

    queens_ball = input("""Queen Elisia, your mother, is having a royal ball in your name, as you are about to be
    crowned the next King of Avendale following your father's passing. The ball starts in around one hour. Will you
    attend the ball? Or will you stay in your room?
    A. Attend Ball.
    B. No! I'll stay in my room where I belong!
    Your choice: """)

    if queens_ball.upper() == "A":
        print("""You take your time and put on the fanciest garments you could find in your wardrobe. You are
        wearing a blouse of the purest red silk and black trousers lined with golden trim around the waist. You
        appear stunning. You walk into the ball room to see your mother's beeming face. She looks very pleased to
        see you!""")
        mother_relationship += 2
        exp = random.randrange(10, 25)
        if exp >= level_1 and exp < level_2:
            print("You are now level 1!")
        elif exp >= level_2 and exp < level_3:
            print("You are now level 2!")

    elif queens_ball.upper() == "B":
        print("""You remain in your room and wait for the ball to begin. You fiddle with the tufts of hair that are
        jutting out of your brown mop. Someone bangs on the door, startling you.""", name,"""! Are you in there!?""")
        choice = input("Do you answer? ")
        if choice.upper() == "Y":
            print("""You respond with 'Yes Mother!'
            Your mother walks into your room with a glistening pearl colored dress with white frills around the neck
            and shoulders. She walks over to you and says: """, name, """, why dont you come down to the ball I
            have arranged for you? You are about to be named the heir to the throne of Avendale. Don't you want
            this? You've wanted to be King since you were a wee child.
            A. """)





    attack = input("Do you want to attack the troll? ")

    if attack == "y":
        exp = random.randrange(45, 100)
        print("You killed a troll, you gained", exp, "experience!")
        lvl_up()


def start_screen():
    print("""Welcome to Dragons and Trolls!""")
    print()
    start = input("Would you like to start a new game? ")
    if start == "y":
        start_game()
    else:
        quit()

if __name__ == "__main__":
    main()