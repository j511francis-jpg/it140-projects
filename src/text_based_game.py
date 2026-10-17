# Display instructions
def show_instructions():
    print("""
Text Adventure Game
Collect all 6 items before finding the villain to win.
Move commands: go North, go South, go East, go West
Add to Inventory: get [item]
Type 'exit' to quit the game
""")


# Display player status
def show_status(current_room, inventory, rooms):
    print("\n---------------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see a", rooms[current_room]["item"])

    print("---------------------------")


def main():

    # Room dictionary
    rooms = {
        'Living Room': {'North': 'Kitchen', 'East': 'Bedroom'},
        'Kitchen': {
            'South': 'Living Room',
            'East': 'Dining Room',
            'item': 'Key'
        },
        'Dining Room': {
            'West': 'Kitchen',
            'North': 'Garage',
            'item': 'Shield'
        },
        'Garage': {
            'South': 'Dining Room',
            'item': 'Helmet'
        },
        'Bedroom': {
            'West': 'Living Room',
            'North': 'Bathroom',
            'item': 'Armor'
        },
        'Bathroom': {
            'South': 'Bedroom',
            'East': 'Office',
            'item': 'Potion'
        },
        'Office': {
            'West': 'Bathroom',
            'North': 'Dungeon',
            'item': 'Sword'
        },
        'Dungeon': {
            'South': 'Office',
            'item': 'Villain'
        }
    }

    # Starting values
    current_room = 'Living Room'
    inventory = []
    total_items = 6

    show_instructions()

    # Main game loop
    while True:

        show_status(current_room, inventory, rooms)

        move = input("Enter your move: ").strip()

        if move.lower() == "exit":
            print("Thanks for playing!")
            break

        command = move.split()

        # Movement command
        if len(command) == 2 and command[0].lower() == "go":

            direction = command[1].capitalize()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]

                # Check if player entered the Dungeon
                if current_room == "Dungeon":

                    if len(inventory) == total_items:
                        print("\nCongratulations!")
                        print("You collected all items and defeated the villain!")
                        print("YOU WIN!")
                    else:
                        print("\Thanks for playing the game. Hope you enjoyed it.")

                    break

            else:
                print("You can't go that way!")

        # Get item command
        elif len(command) >= 2 and command[0].lower() == "get":

            item_name = " ".join(command[1:])

            if (
                "item" in rooms[current_room]
                and rooms[current_room]["item"] == item_name
            ):
                inventory.append(item_name)
                print(item_name, "collected!")

                del rooms[current_room]["item"]

            else:
                print("That item is not in this room.")

        # Invalid command
        else:
            print("Invalid command. Try 'go North' or 'get Key'.")


# Run game
