import time
import random


def print_with_delay(message):
    print(message)
    time.sleep(1.5)


def game_intro(enemy):
    print_with_delay("You find yourself standing in an open field, filled with"
                     "grass and yellow wildflowers.")
    print_with_delay(f"Rumor has it that a {enemy} is somewhere around here, "
                     "and has been terrifying the nearby village.")
    print_with_delay("In front of you is a house.")
    print_with_delay("To your right is a dark cave.")
    print_with_delay("In your hand you hold your trusty (but not very "
                     "effective) dagger.\n")


def return_to_field():
    print_with_delay("You walk back out to the field.\n")


def choose_path(items, enemy, weapon):
    print_with_delay("Enter 1 to knock on the door of the house.")
    print_with_delay("Enter 2 to peer into the cave.")
    print_with_delay("What would you like to do?")
    check_path_choice(items, enemy, weapon)


def check_path_choice(items, enemy, weapon):
    print_with_delay("(Please enter 1 or 2.)")
    response = input()
    if response == "1":
        explore_house(items, enemy, weapon)
    elif response == "2":
        explore_cave(items, enemy, weapon)
    else:
        check_path_choice(items, enemy, weapon)


def explore_house(items, enemy, weapon):
    print_with_delay("You approach the door of the house.")
    print_with_delay("You are about to knock when the door opens and out "
                     f"steps a {enemy}.")
    print_with_delay(f"Eep! This is the {enemy}'s house!")
    print_with_delay(f"The {enemy} attacks you!")
    if weapon not in items:
        print_with_delay("You feel a bit under-prepared for this, what with"
                         " only having a tiny dagger.")
    decide_fight_or_run_away(items, enemy, weapon)


def decide_fight_or_run_away(items, enemy, weapon):
    response = input("Would you like to (1) fight or (2) run away?\n")
    if response == "1":
        fight(items, enemy, weapon)
    elif response == "2":
        run_away(items, enemy, weapon)
    else:
        decide_fight_or_run_away(items, enemy, weapon)


def explore_cave(items, enemy, weapon):
    print_with_delay("You peer cautiously into the cave.")
    if weapon in items:
        print_with_delay("You've been here before, and gotten all the good "
                         "stuff. It's just an empty cave now.")
        return_to_field()
        choose_path(items, enemy, weapon)
    else:
        items.append(weapon)
        print_with_delay("It turns out to be only a very small cave.")
        print_with_delay("Your eye catches a glint of metal behind a rock.")
        print_with_delay(f"You have found the magical {weapon} of {enemy}!")
        print_with_delay("You discard your silly old dagger and take the "
                         f"{weapon} with you.")
        return_to_field()
        choose_path(items, enemy, weapon)


def fight(items, enemy, weapon):
    if weapon in items:
        print_with_delay("As the troll moves to attack, you unsheathe your"
                         f" new {weapon}.")
        print_with_delay(f"The {weapon} of {enemy} shines brightly in your"
                         " hand as you brace yourself for the"
                         " attack.")
        print_with_delay(f"But the {enemy} takes one look at your shiny new"
                         " toy and runs away!")
        print_with_delay(f"You have rid the town of the {enemy}. "
                         "You are victorious!\n")
        replay()
    else:
        print_with_delay("You do your best...")
        print_with_delay(f"but your dagger is no match for the {enemy}.")
        print_with_delay("You have been defeated!\n")
        replay()


def run_away(items, enemy, weapon):
    print_with_delay("You run back into the field. Luckily, you don't seem to"
                     " have been followed.\n")
    choose_path(items, enemy, weapon)


def replay():
    response = input("Would you like to play again? (y/n)\n")
    if response.lower() == "y":
        print_with_delay("Excellent! Restarting the game ...\n")
        start_game()
    elif response.lower() == "n":
        print_with_delay("Thanks for playing! See you next time.\n")
    else:
        replay()


def start_game():
    items = []
    enemies = ["troll", "wicked fairy", "pirate", "gorgon", "dragon"]
    weapons = ["sword", "wand", "spear"]
    enemy = random.choice(enemies)
    weapon = random.choice(weapons)
    game_intro(enemy)
    choose_path(items, enemy, weapon)


start_game()
