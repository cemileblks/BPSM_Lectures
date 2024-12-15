#!/usr/bin/python3

#1: Interrogating the user...

# With the aid of a function and a dictionary, write an interactive Python programme/script that will ask the user the following questions
# What's your name?
# How old are you?
# What is your favourite colour?
# Do you like Python?
# The world is flat: True or False?
# and then, based on their answers, make some comments back to them (this doesn't have to be at all serious, it's the methods used that we are trying out here....!)

import os

os.system('clear')

print("\n\nImported os\n\n")

def user_questions():
    user_info = {}
    user_name = input("What is your name? ")
    print(f"Your name is {user_name}\n\n") 
    user_info["name"] = user_name

    user_age = input("How old are you? ")
    print(f"You are {user_age} years old, or are you?\n\n")
    user_info["age"] = user_age

    user_color = input("What is your favourite color? ")
    print(f"Your fav color is {user_color}\n\n")
    user_info["fav_color"] = user_color

    more_info = input("Do you like Python? Yes/No ")
    more_info = more_info.lower()
    if more_info == "no":
        print(f"I am sorry that you don't like python\n\n")
        mad_lip_python = "but also run for your life!"
    elif more_info == "yes":
        print(f"Glad you agree that python is cool...\n\n")
        mad_lip_python = "but it is your friend so don't worry."
    else:
        print(f"That wasn't a yes/no answer! :((\n\n")
        mad_lip_python = "it can be a friend or foe..."
    user_info["likes_python"] = more_info

    flat_world = input("The world is flat: True or False? ")
    flat_world = flat_world.lower()

    if flat_world == "true":
        print(f"That was proved false years ago, pls look it up!\n\n")
        mad_lip_flat = "flat and will go on forever."
    elif flat_world == "false":
        print(f"I'm glad you know that the world is not flat\n\n")
        mad_lip_flat = "round and if you run straight you'll be be back here decades later!"
    else:
        print(f"That wasn't a true false response! :((\n\n")
        mad_lip_flat = "unknown, can be flat can be round or any other shape, don't think we will ever know..."
    user_info["world_flat"] = flat_world

    print("Here is a short story I wrote for you:\n\n")

    print(f"""\t{user_info.get('name')} is {user_info['age']} but they might as well be lying! Your fav color {user_info['fav_color']} is really boring, please look into more colors (JK). Beware of the python behind you {mad_lip_python} Your world is {mad_lip_flat}\n\n""")
    return user_info

user_info = user_questions()
print("This is the dictionary generated using your input:\n\t", user_info)