# This is the list that all of the rooms in the game will be appended to
room_list = []

# List of all rooms in the game
room = ["You are in a dark, cryptic room with a door to the north and a door to the east.", 3, 1, None, None]
room_list.append(room)

room = ["You walk out into a long hallway. There are doors to the north, east, and south.", 4, 2, None, 0]
room_list.append(room)

room = ["You enter a Sun Room. There are doors to the north and west.", 5, None, None, 1]
room_list.append(room)

room = ["You enter a kitchen. The floor is littered with cooking utensils and there are scratch marks on the floor."
        " There are doors to the east and south.", None, 4, 0, None]
room_list.append(room)

room = ["You enter someone's bedroom. There are doors to the north, east, south, and west.", 6, 5, 1, 3]
room_list.append(room)

room = ["You enter a basement. There are sets of stairs accompanied by doors to the south and to the west.",
        None, None, 2, 4]
room_list.append(room)

room = ["You walk out of the house and onto a pattio. There is a door to the south.", None, None, 4, None]
room_list.append(room)

# Starting Room
current_room = 0

done = False

# Traveling throughout the house
while not done:
    print(room_list[current_room][0])
    print()
    room_choice = input("Which direction would you like to travel? ")
    print()

# These dictates where the player wants to travel and where they cannot travel.
    if room_choice.upper() == "N" or room_choice.upper() == "NORTH":
        next_room = room_list[current_room][1]
        print()
        if next_room == None:
            print("You cannot go that direction. There is no door there!")
            print()
        else:
            current_room = next_room

    elif room_choice.upper() == "E" or room_choice.upper() == "EAST":
        next_room = room_list[current_room][2]
        print()
        if next_room == None:
            print("You cannot go that direction. There is no door there!")
            print()
        else:
            current_room = next_room

    elif room_choice.upper() == "S" or room_choice.upper() == "SOUTH":
        next_room = room_list[current_room][3]
        print()
        if next_room == None:
            print("You cannot go that direction. There is no door there!")
            print()
        else:
            current_room = next_room

    elif room_choice.upper() == "W" or room_choice.upper() == "WEST":
        next_room = room_list[current_room][4]
        print()
        if next_room == None:
            print("You cannot go that direction. There is no door there!")
            print()
        else:
            current_room = next_room

# If player would like to quit the game
    elif room_choice.upper() == "Q" or room_choice.upper() == "QUIT":
        print("You have quit the game.")
        done = True

# If player chooses to travel somewhere that they cannot travel
    else:
        print("That is not a direction you can travel!")
        print()




