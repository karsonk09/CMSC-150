import random


# End sequence
def game_over():
    end = input("Would you like to play again? (Y/N) ")
    if end.upper() == "Y":
        main()
    if end.upper() == "N":
        print("GAME OVER")


# Intro to game
def main():
    print("Welcome to Pirates!")
    print("You have stolen gold and a boat from a local band of pirates in Havana.")
    print("The pirates want their gold back and are chasing you down with their ships!")
    print("You must travel across the Golden Sea to escape the pirates!")
    print("Survive your ocean adventure and enjoy the spoils of your efforts.")




    done = False

    # Variables
    player_hunger = 0
    boat_condition = 0
    miles_traveled = 0
    dist_traveled_p = -20
    food_reserves = 4

    # Player choices
    while not done:
        print()
        print("A. Eat from your reserves.")
        print("B. Ahead half sail.")
        print("C. Ahead full sail.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        choice = input("What is your choice? ")
        print()

        # Player chooses to quit
        if choice.upper() == "Q":
            done = True

        # Player chooses to do a status check
        elif choice.upper() == "E":
            print("You have traveled ", miles_traveled, "miles.")
            print("You have ", food_reserves, "food left in your reserves.")
            print("The pirates are ", miles_traveled - dist_traveled_p, "miles behind you.")

        # Player chooses to rest
        elif choice.upper() == "D":
            boat_condition = 0
            print("You have made repairs to your boat.")
            dist_traveled_p += random.randrange(8, 15)

        # Player chooses to travel at full sail
        elif choice.upper() == "C":
            miles_turn = random.randrange(11, 19)
            miles_traveled += miles_turn
            print("You have traveled ", miles_turn, "miles!")
            player_hunger += 1
            boat_condition += random.randrange(1, 4)
            dist_traveled_p += random.randrange(8, 15)
            # Island
            if not done and player_hunger < 6 and boat_condition < 8:
                island = random.randrange(1, 21)
                if island == 9:
                    print("You have found an island!")
                    food_reserves = 4
                    player_hunger = 0
                    boat_condition = 0

        # Player chooses to travel at half sail
        elif choice.upper() == "B":
            miles_turn = random.randrange(4, 12)
            miles_traveled += miles_turn
            print("You have traveled ", miles_turn, "miles!")
            player_hunger += 1
            boat_condition += 1
            dist_traveled_p += random.randrange(7, 15)
            # Island
            if not done and player_hunger < 6 and boat_condition < 8:
                island = random.randrange(1, 21)
                if island == 9:
                    print("You have found an island!")
                    food_reserves = 4
                    player_hunger = 0
                    boat_condition = 0

        # Player chooses to eat from reserves
        elif choice.upper() == "A":
            if food_reserves == 0:
                print("You have no more food left in your reserves!")
            elif food_reserves > 0:
                print("You eat food from your reserves.")
                player_hunger = 0
                food_reserves -= 1

        # Player hunger
        if player_hunger > 4 and player_hunger <= 6:
            print("You are hungry.")

        elif player_hunger > 6:
            print("You have died of hunger.")
            done = True
            game_over()

        # Boat condition
        if boat_condition > 5 and boat_condition <= 8:
            print("Your boat is wearing down.")

        elif boat_condition > 8:
            print("Your boat has sunk!")
            done = True
            game_over()

        # Pirates distance
        if dist_traveled_p >= miles_traveled:
            print("The pirates have caught you!")
            done = True
            game_over()

        elif dist_traveled_p >= miles_traveled - 15 and dist_traveled_p < miles_traveled:
            print("The pirates are close behind!")

        # Winning the game
        if miles_traveled >= 200:
            print("Congratulations! You have made it across the Golden Sea!")
            print("You win!")
            done = True
            game_over()

if __name__ == "__main__":
    main()