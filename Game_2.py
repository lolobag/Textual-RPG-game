
# Pyhton Text RPG

import pygame
import cmd
import textwrap
import sys
import os
import time
import random


screen_width = 100

#### Player Setup ####
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False
        
myPlayer = player()

#### Title Screen ####
def title_screen_selection():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game() # placeholder until written #
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game() # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print("############################")
    print("# Welcome to the Text RPG! #")
    print("############################")
    print("- Play -                    ")
    print("- Help -                    ")
    print("- Quit-                     ")
    print(" Copyright 2019 lolobag.lol ")
    title_screen_selection()

def help_menu():
    print("############################")
    print("# Welcome to the Text RPG! #")
    print("############################")
    print("- Use UP, DOWN, LEFT, RIGHT to move")
    print("- Type your commands to do them")
    print("- Use ""look"" to inspect something")
    print("- Good luck and have fun")
    title_screen_selection()

#### Game functionality ####
def setup_game():
    return



#### MAP ####
"""
a1  a2 ... # PLAYER STARTS AT b2 #
_____________
|  |  |  |  | a4
_____________
|  | x|  |  | b4 ...
_____________
|  |  |  |  |
_____________
|  |  |  |  |
_____________
"""



ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

solved_places = {"a1": False, "a2": False, "a3": False, "a4": False,
                "b1": False, "b2": False, "b3": False, "b4": False,
                "c1": False, "c2": False, "c3": False, "c4": False,
                "d1": False, "d2": False, "d3": False, "d4": False,
                }

znonename = {
        "a1":{
            ZONENAME: "Town Market",
            DESCRIPTION: "This is market with stores!",
            EXAMINATION: "Search the stores!",
            SOLVED: False,
            UP: "",
            DOWN: "b1",
            LEFT: "",
            RIGHT: "a2",
        },
         "a2":{
            ZONENAME: "Town Entrance",
            DESCRIPTION: "Big gate!",
            EXAMINATION: "Nothing to see but the door",
            SOLVED: False,
            UP: "",
            DOWN: "b2",
            LEFT: "a1",
            RIGHT: "a3",
        },
         "a3":{
            ZONENAME: "Town Square.",
            DESCRIPTION: "There is a round fountain, and lots of people!",
            EXAMINATION: "See the fountan, and talk to the people.",
            SOLVED: False,
            UP: "",
            DOWN: "b3",
            LEFT: "a2",
            RIGHT: "a4",
        },
         "a4":{
            ZONENAME: "Town Hall",
            DESCRIPTION: "Big building with the Mayor!",
            EXAMINATION: "Search the building, talk to the Mayor.",
            SOLVED: False,
            UP: "",
            DOWN: "b4",
            LEFT: "a3",
            RIGHT: "",
        },
         "b1":{
            ZONENAME: "Field",
            DESCRIPTION: "Open field, lots of grass!",
            EXAMINATION: "Look for something.",
            SOLVED: False,
            UP: "a1",
            DOWN: "c1",
            LEFT: "",
            RIGHT: "b2",
        },
         "b2":{
            ZONENAME: "Home",
            DESCRIPTION: "This is your home!",
            EXAMINATION: "Your home is the same - nothing has changed.",
            SOLVED: False,
            UP: "a1",
            DOWN: "c3",
            LEFT: "b1",
            RIGHT: "b3",
        },
         "b3":{
            ZONENAME: "Residences",
            DESCRIPTION: "Hoses where people live!",
            EXAMINATION: "Nothing to examine it is rude to look in other peoples hoses.",
            SOLVED: False,
            UP: "a4",
            DOWN: "c3",
            LEFT: "b2",
            RIGHT: "b4",
        },
         "b4":{
            ZONENAME: "Park",
            DESCRIPTION: "Trees, walking pad, a small lake!",
            EXAMINATION: "Look for hidden treasures",
            SOLVED: False,
            UP: "a4",
            DOWN: "c4",
            LEFT: "b3",
            RIGHT: "",
        },
     

}

#### GAME INTERACTIVITY ####
def print_location ():
    print("\n" + ("#" * (4 + len(myPlayer.location))))
    print("# " + myPlayer.location.upper() + " #")
    print("# " + zonemap [my.Player.position][DESCRIPTION] + " #")
    print("\n" + ("#" * (4 + len(myPlayer.location))))    

def prompt():
    print("\n" + "=========================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ["move", "go", "travel", "walk", "quit", "examine", "quit", "inspect", "interact", "look"]
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again, \n")
        action = input("> ")
    if action.lower() == "quit":
        sys.exit()
    elif  action.lower() in ["move", "go", "travel," "walk"]:
        player_move(action.lower())
    elif action.lower() in ["examine", "quit", "inspect", "interact", "look"]:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ["up", "north"]:
        destination = zonemap[myPlayer.location][UP]
        movmenet_handler(destination)
    elif dest in ["left", "west"]:
        destination = zonemap[myPlayer.location][LEFT]
        movmenet_handler(destination)
    elif  dest in ["east", "right"]:
        destination = zonemap[myPlayer.location][RIGHT]
        movmenet_handler(destination)
    elif dest in ["south", "down"]:
        destination = zonemap[myPlayer.location][DOWN]
        movmenet_handler(destination)


def movmenet_handler(destination):
    print("\n" + "You have move to the " + destination + ".")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have exhausted this zone.")
    else:
        print("You can trigger puzzle here!")


#### GAME FUNCTIONALATY ####


def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        # Here handel if puzlle has been solved, boos defeted, expolres evrithing, ect...


def setup_game():
    os.system('clear')

    ### Name colecting
    qustion1 = "What is your name?\n"
    for character in qustion1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer = player_name

    qustion2 = "Hello what role do you want to play?\n"
    qustion2added = "(You can play as: warrior, mage or priest)\n"
    for character in qustion2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in qustion2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ["warrior", "mage", "priest"]
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a " + player_job + "!\n")
       

    #### PLAYER STATUS
    if myPlayer.job is "worior":
        self.hp = 120
        self.mp = 20
    elif myPlayer.job is "mage":
        self.hp = 40
        self.mp = 120
    elif myPlayer.job is "priest":
        self.hp = 60
        self.mp = 60


    #### INTRUDUCTION

    player_name = myPlayer
    player_job = myPlayer.job

    qustion3 = "welcome" + player_name + " the " + player_job + ".\n"
    for character in qustion3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   
    speech1 = "Welcome to this fantasy world!\n"
    speech2 = "I hope it greatse you well!\n"
    speech3 = "Yust make shure you dont get lost...\n"
    speech4 = "Muahahahaha...\n"
    for character in speech1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
    player_name = input("> ")
    myPlayer = player_name
    for character in speech2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
    player_name = input("> ")
    myPlayer = player_name
    for character in speech3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
    player_name = input("> ")
    for character in speech4:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.2)
    player_name = input("> ")
    myPlayer = player_name

    os.system("clear")
    print("###################")
    print("# Lets start now! #")
    print("###################")
    main_game_loop()

title_screen()



