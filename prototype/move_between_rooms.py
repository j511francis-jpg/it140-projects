"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# Start the player in the Great Hall
current_room = 'Great Hall'

# Gameplay loop
while current_room != 'exit':

    # Display current room
    print('\nYou are in the', current_room)

    # Get player command
    command = input('Enter a direction (north, south, east, west) or exit: ')

    # Exit game
    if command == 'exit':
        current_room = 'exit'

    # Move to another room if the direction is valid
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]

    # Invalid command
    else:
        print('Invalid command!')

# End game message
print('Thanks for playing!')
