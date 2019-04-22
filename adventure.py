# -*- coding: utf-8 -*-
"""
Text Adventure Game
An adventure in making adventure games.

To test your current solution, run the `test_my_solution.py` file.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Shelby Kline
"""
__version__ = 8

# 2) print_introduction: Print a friendly welcome message for your game
# intro to game, gives a little bit of background so the player can 
# think about where they need to go
def print_introduction():
    print("~ ~ ~ ~ ~")
    print("You are a old, slow-moving possum.")
    print("You live in a treehouse located in the middle of the woods.")
    print("It's almost dinner time and it's raining.")
    print("Do you have food? Do you have a raincoat?")
    print("You don't remember.")
    print("I guess you will just have to find out.")
    print("Remember, you can enter 'quit' to stop at any point.")
    print("~ ~ ~ ~ ~")

# 3) get_initial_state: Create the starting player state dictionary
# the status_dictionary will change if the user...
# finds the raincoat, finds food, changes location based on the command they input,
# or wins, loses, or quits the game    
def get_initial_state():
    status_dictionary = {"game status": "playing",
                         "food": False,
                         "raincoat": False,
                         "location": "your room"}
    return status_dictionary

# 4) print_current_state: Print some text describing the current game world
# accepts status_dictionary, prints about where you are and sometimes how you got there
def print_current_state(status_dictionary):
    # the following text is just to avoid sentences like "you are in the outside" or "you are in the your room"
    if (status_dictionary["location"])== "kitchen" or (status_dictionary["location"])== "mudroom":
        print("You are in the " + (status_dictionary["location"])+ ".")
    if (status_dictionary["location"])== "your room":
        print("You are in " + (status_dictionary["location"])+ ".")
    if (status_dictionary["location"]) == "outside":
        print("You are " + (status_dictionary["location"])+ ".")
    if (status_dictionary["location"]) == "market":
        print("You are at the " + (status_dictionary["location"])+ ".")
# the following text are decriptors for each room
    if(status_dictionary["location"]=="your room"):
        print("It's pretty nice for North America's only marsupial.")
    if(status_dictionary["location"]=="home"):
        print("You are inside your house.")
    if(status_dictionary["location"]=="home") and status_dictionary["food"]==False:
        print("You took the wrong turn and ended up back at home.")
    if(status_dictionary["location"]=="outside"):
        print("It's downpouring out here.")
    if(status_dictionary["location"]=="mudroom") and status_dictionary["food"]==False:
        print("You found your raincoat!")
        print("You should be able to go outside now...")
    if(status_dictionary["location"]=="mudroom") and status_dictionary["food"]==True:
        print("You put your raincoat back.")
    if(status_dictionary["location"]=="kitchen") and (status_dictionary["food"]==False):
        print("Your kitchen is a little dirty.")
        print("There's no food here.")
        print("Meh. You'll have to look elsewhere.")
    if(status_dictionary["location"]=="path") and (status_dictionary["food"]==False):
        print("You are heading towards the market.")
    if(status_dictionary["location"]=="path") and (status_dictionary["food"]==True):
        print("You are heading home.")
    if(status_dictionary["location"]=="market"):
        print("There are lots of different booths.")
        print("You gravitate towards the booth selling bugs...")
        print("You're a possum, remember? That's what you eat. Don't be so grossed out.")
        print("You buy some bugs from the seller and thank them.")
        print("Time to go home.")

# 5) get_options: Return a list of commands available to the player right now
# based on location, it returns a certain list of options that
# will be printed in print_options
def get_options(status_dictionary):
    if(status_dictionary["location"]=="your room"):
        return ["Go to kitchen","Go outside", "Go to mudroom"]
    if(status_dictionary["location"]=="kitchen") and (status_dictionary["food"]==False):
        return ["Go to mudroom"]
    if(status_dictionary["location"]=="mudroom"):
        return ["Go to your room"]
    if(status_dictionary["location"]=="outside"):
        return ["Go to path"]
    if(status_dictionary["location"]=="path"):
        return ["Go left", "Go right"]
    if(status_dictionary["location"]=="market"):
        return ["Return to path"]
    if(status_dictionary["location"]=="path") and (status_dictionary["food"]==True):
        return ["Go left", "Go right"]
    if(status_dictionary["location"]=="home") and (status_dictionary["food"]==True):
        return ["Go to kitchen", "Go to your room", "Go to mudroom"]
    if(status_dictionary["location"]=="home") and (status_dictionary["food"]==False):
        return ["Go to kitchen", "Go to your room", "Go to mudroom", "Go outside"]
    
    
# 6) print_options: Print out the list of commands available    
#print what you return in get_options using a for loop
# to go through each option in the list from get_options
def print_options(a_list):
    print("Choose one:")
    for option in a_list:
        print(option)

# 7) get_user_input: Repeatedly prompt the user to choose a valid command
#take in commands, process commands
# a while loop is used because True will always be true
# so command will always be what the user puts in input
def get_user_input(a_list):  
    while True:
        command = input()
        if command in a_list:
            return command
        elif command == "quit":
            return command
            
# 8) process_command: Change the player state dictionary based on the command, if statements
#using if statements, the "food" or "raincoat" changes if the user
#picks the right command to go to the right location
def process_command(command, status_dictionary):
    if command == "Go to kitchen":
        status_dictionary["location"]="kitchen"
        if status_dictionary["food"]==True:
            status_dictionary["game status"]="win"
    if command == "Go to mudroom":
        status_dictionary["location"]="mudroom"
        status_dictionary["raincoat"]=True
    if command == "Go to your room":
        status_dictionary["location"]="your room"
    if command == "Go to kitchen":
        status_dictionary["location"]="kitchen"
    if command == "Go outside":
        if status_dictionary["raincoat"]==False:
            status_dictionary["game status"]="lose"
        else:
            status_dictionary["location"]="outside"
    if command == "Go to path":
        status_dictionary["location"]="path"
    if command == "Go left":
        status_dictionary["location"]="market"
        status_dictionary["food"]=True
    if command == "Go right": 
        status_dictionary["location"]="home"
    if command == "Return to path":
        status_dictionary["location"]="path"
    if command == "Return home":
        status_dictionary["location"]="your room"
    if command == "quit":
        status_dictionary["game status"]="quit"
    
    
# 9) print_game_ending: Print a victory, lose, or quit message at the end
#prints the outcome of lose, win, victory, quit
def print_game_ending(status_dictionary):
    if status_dictionary["game status"] == "win":
        print ("You made dinner!")
        print("You're warm and dry inside, away from the rain.")
        print("You survived another day as a possum. You won!")
    if status_dictionary["game status"] == "quit":
        print("You gave up.")
        print("You didn't find food, so you starved.")
        print("Try again, maybe?")
    if status_dictionary["game status"] == "playing":
        print("You're playing this game.")
    if status_dictionary["game status"] == "lose":
        print("You didn't find your raincoat, so now you're soaked.")
        print("You're also not very visible in this rain...")
        print("...and your surroundings aren't easy to navigate...")
        print("You're completely drenched and lost.")
        print("You lost.")
        print("Try again, maybe?")
# Command Paths to give to the unit tester
WIN_PATH = ["Go to mudroom", "Go to your room", "Go outside", "Go to path", "Go left", "Return to path", "Go right", "Go to kitchen"] 
LOSE_PATH = ["Go outside"]

# 1) Main function that runs your game, read it over and understand
# how the player state flows between functions.
def main():
    # Print an introduction to the game
    print_introduction()
    # Make initial state
    the_player = get_initial_state()
    # Check victory or defeat
    while the_player['game status'] == 'playing':
        # Give current state
        print_current_state(the_player)
        # Get options
        available_options = get_options(the_player)
        # Give next options
        print_options(available_options)
        # Get Valid User Input
        chosen_command = get_user_input(available_options)
        # Process Commands and change state
        process_command(chosen_command, the_player)
    # Give user message
    print_game_ending(the_player)

# Executes the main function
if __name__ == "__main__":
    '''
    You might comment out the main function and call each function
    one at a time below to try them out yourself '''
    main()
    ## e.g., comment out main() and uncomment the line(s) below
    # print_introduction()
    # print(get_initial_state())
    # ...