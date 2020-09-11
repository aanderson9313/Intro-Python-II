from room import Room
from player import Player
from item import Item 
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber!"""),
}


# Link rooms together
def set_up_rooms():
    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside']
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure'] 
    room['treasure'].s_to = room['narrow']


# add items/treasure/ mostly useful stuff to rooms 
def add_room_items():
    room['outside'].add_item(Item("Stick", f" A meager weapon to fend off the possible wolves...just kidding...\n there aren't any wolves...or are there?"))
    room['foyer'].add_item(Item("Potion", f" An elixir to heal your wounds from the wolves..."))
    room['foyer'].add_item(Item("Empty Satchel", f" A bag left behind by the previous adventurer\n ...possibly eaten by wolves."))
    room['overlook'].add_item(Item("Shield", f"A large wooden shield emblazened with a majestic steed."))
    room['narrow'].add_item(Item("Sword", f" A sharp blade that hums with the blood of your enemies...or possibly wolves blood."))
    room['narrow'].add_item(Item("compass", f"A small instrument used for guiding adventurers away from the wolves and back to sanctuary."))
    room['treasure'].add_item(Item("Book", f"SAS Survival Handbook, Third Edition: The Ultimate Guide to Surviving Anywhere, by John 'Lofty' Wiseman."))
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ['n', 'e', 's', 'w']
actions = ['take', 'drop', 'examine']

player_name = input('Welcome adventurer! What is your name?')
player = Player(player_name, room['outside'])
print(f"Good Luck, {player_name}! Your Journey begins to the north!\n Make sure to keep an eye out for items along the way to help on your journey!")
set_up_rooms()
add_room_items()
player.look()


while True:
    user_input = input(f"Which area would you like to visit? ").lower().split()
    if len(user_input) > 2 or len(user_input) < 1:
            print(f"Sorry, {player.name}, that location/command is not valid. 'help' is available should you wish to use it")
    
    elif len(user_input) == 2:
        if user_input[0] in actions:
            if user_input[0] == 't' or user_input[0] == 'take':
                item = player.select_inventory_item(user_input[1])
                player.take(item)
                
            elif user_input[0] == 'd' or user_input[0] == 'drop':
                item = player.select_inventory_item(user_input[1])
                player.drop(item)
    else: 
        if user_input[0] == "q" or user_input[0] == "quit":
                print(f'Thanks for playing {player.name}! See you on your next adventure!')
                break
        elif user_input[0] == 'l' or user_input[0] == 'look':
                player.look()
                continue
        elif user_input[0] ==  'i' or user_input[0] == 'inventory':
                player.show_inventory()
                
            
        elif user_input[0] == 'h' or user_input[0] == 'help':
                print('Commands:\n "n" -move North\n "s" -move South\n "e" -move East\n "w" -move West\n "h" or "help" -Help Menu\n "q" or "quit" -Exit Game\n "t" or "take" -Take Item\n "d" or "drop" -Drop Item\n "i" or "inventory" -Examine inventory\n "l" or "look" -Look around the current room\n')
                continue
            
        elif user_input[0] in directions:
            try:
                player.move(user_input[0])
                print(f'You are in the {player.current_room.name}. \n{player.current_room.description}')
            except AttributeError:
                print(f'{player.name}, your journey awaits you, please select another direction!')
           
        else:
            print('Movement not allowed, please enter a valid destination (n, e, s, w) to move around the map')