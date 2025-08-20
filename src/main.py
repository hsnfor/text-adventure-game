# The Python Labyrinth - Text-Based Adventure Game
# Phase 2: World Engine

# A dictionary to hold the player's inventory
inventory = []

# A dictionary linking a room to other rooms and any item it contains
# This is the data structure that defines our game world
rooms = {
    'Kitchen': {
        'south': 'Hallway',
        'item': 'key',
        'description': 'You are in the Kitchen. It smells of old food. A single key glints on the counter.'
    },
    'Hallway': {
        'north': 'Kitchen',
        'east': 'Living Room',
        'south': 'Garden',
        'item': None,  # No item in this room
        'description': 'You are in a dusty Hallway. There are doors to the north, east, and south. The south door is locked.'
    },
    'Living Room': {
        'west': 'Hallway',
        'item': 'book',
        'description': 'You are in a cozy Living Room. A large, interesting-looking book is on the coffee table.'
    },
    'Garden': {
        'north': 'Hallway',
        'item': None,
        'description': 'You are in the beautiful Garden! You win! Fresh air! Sunshine!'
    }
}

# The player starts in the Kitchen
current_room = 'Kitchen'

# Main game function
def main():
    show_instructions()
    game_loop()

# Function to show the game instructions
def show_instructions():
    print("=" * 50)
    print("           The Python Labyrinth")
    print("=" * 50)
    print("Commands:")
    print("  go [direction] - Move in a direction (north, south, east, west)")
    print("  get [item]     - Pick up an item")
    print("  look           - Look around the room again")
    print("  inventory      - Check your inventory")
    print("  quit           - Exit the game")
    print("=" * 50)
    print("Find a way to escape to the Garden!")
    print("")

# The core game loop
def game_loop():
    global current_room

    # Show the description of the starting room
    show_status()

    while True:
        # Get the player's next command
        print("----------------------------------------")
        command = input("What would you like to do? ").strip().lower().split(' ', 1)
        # The command is split into a list. e.g., 'go north' becomes ['go', 'north']

        # Handle the 'quit' command
        if command[0] == 'quit':
            print("Thanks for playing!")
            break

        # Handle the 'go' command
        elif command[0] == 'go':
            if len(command) > 1:
                move_player(command[1])
            else:
                print("Go where? Please specify a direction.")

        # Handle the 'get' command
        elif command[0] == 'get':
            if len(command) > 1:
                get_item(command[1])
            else:
                print("Get what? Please specify an item.")

        # Handle the 'inventory' command
        elif command[0] == 'inventory':
            show_inventory()

        # Handle the 'look' command
        elif command[0] == 'look':
            show_status()

        # Handle unknown commands
        else:
            print("I don't understand that command. Try 'go', 'get', 'inventory', 'look', or 'quit'.")

        # Check for win condition (player is in the Garden with the key)
        if current_room == 'Garden' and 'key' in inventory:
            print("\n" + "=" * 50)
            print("You used the key to unlock the door!")
            print("YOU HAVE ESCAPED THE PYTHON LABYRINTH!")
            print("Congratulations, you win!")
            print("=" * 50)
            break
        elif current_room == 'Garden' and 'key' not in inventory:
            print("The door to the garden is locked. You need a key to open it.")
            # Move the player back to the Hallway if they try to enter without the key
            current_room = 'Hallway'
            show_status()

# Function to show the player's current status (location and inventory)
def show_status():
    print("\n" + rooms[current_room]['description'])
    if rooms[current_room]['item'] is not None and rooms[current_room]['item'] not in inventory:
        print(f"You see a {rooms[current_room]['item']} here.")

# Function to show the player's inventory
def show_inventory():
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Inventory:", ', '.join(inventory))

# Function to move the player between rooms
def move_player(direction):
    global current_room
    if direction in rooms[current_room]:
        new_room = rooms[current_room][direction]
        current_room = new_room
        print(f"You go {direction}.")
        show_status()
    else:
        print("You can't go that way!")

# Function to get an item from a room
def get_item(item_name):
    if rooms[current_room]['item'] == item_name and item_name not in inventory:
        inventory.append(item_name)
        print(f"You picked up the {item_name}!")
        # Optionally, you can set the room's item to None after picking it up
        # rooms[current_room]['item'] = None
    elif item_name in inventory:
        print(f"You already have the {item_name}.")
    else:
        print(f"You don't see a {item_name} here.")

# This line ensures the game starts when you run the script
if __name__ == "__main__":
    main()
