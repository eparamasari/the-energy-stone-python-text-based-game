import time
import random

items = []
villain_choices = ["night zombies", "vampires",
                   "joker wannabees", "dark witches", "dementors"]
villains = random.choice(villain_choices)
new_stones = ["solar", "wind", "wave", "biofuel", "geothermal"]
new_stone = random.choice(new_stones)


def print_wait(message, delay):
    print(message)
    time.sleep(delay)


def intro():
    print_wait("You arrive at the dark night village.", 2)
    print_wait("The village has been dark for months,", 1)
    print_wait("as someone stole their energy stone.", 2)
    print_wait(f"People say {villains} have been "
               "terrorizing them at night.", 3)
    print_wait("You have your coal stone, it's not very strong but...", 1)
    print_wait("you hope you will be able to light up the village with it.", 3)
    print_wait("You see the village hall on the left,", 0.5)
    print_wait("and a field on the right.", 2)


def get_destination():
    destination = input("Where would you like to go?\n"
                        "Enter 1 to go to the village hall.\n"
                        "Enter 2 to go to the field.\n")
    if destination == '1':
        village_hall()
    elif destination == '2':
        field()
    else:
        print_wait("Sorry, I don't understand.", 1)
        get_destination()


def village_hall():
    print_wait("You walk to the village hall.", 2)
    print_wait("The village head asks you if you have", 1)
    print_wait("an energy stone to light up their village.", 2)
    if new_stone in items:
        print_wait(f"You give your {new_stone} energy "
                   "stone to the village head.", 2)
        print_wait("He puts it in the casebox, and it lits "
                   "the village so bright.", 2)
        print_wait("A few hours later, night comes,", 2)
        print_wait(f"and {random.randint(100, 1000)} {villains} "
                   "are seen approaching", 2)
        print_wait(f"The {new_stone} energy stone power is so strong "
                   f"that the {villains} are fended off and died.", 5)
        print_wait("The villagers look so happy. They think you're a hero.", 2)
        print_wait("Congratulations, you did it! You saved the village!", 2)
        play_again()
    else:
        print_wait("Would you:", 1)
        print_wait("(1) give them your coal stone or...", 2)
        print_wait("(2) tell them you need to find one?", 2)
        give_coal_stone = input("Please enter 1 or 2.\n").lower()
        if '1' in give_coal_stone:
            print_wait("You give your coal stone to the village head.", 2)
            print_wait("He puts it in the casebox, and it lits.", 2)
            print_wait("A few hours later, night comes,", 2)
            print_wait(f"and {random.randint(100, 1000)} {villains} "
                       "are seen approaching", 2)
            print_wait("Unfortunately, the coal stone power "
                       f"is not strong enough to drive away the {villains}", 5)
            print_wait("I'm sorry, but you have failed.", 1)
            print_wait("\"Game Over\"", 2)
            play_again()
        if '2' in give_coal_stone:
            print_wait("You tell him you still need to find one.", 2)
            print_wait("You then leave the village hall.", 2)
            get_destination()


def field():
    print_wait("You walk to the field, passing through "
               "the green grass and blue flowers.", 2)
    print_wait("You see a rusty copper chest under a tree.", 2)
    print_wait("You walk to the chest and open it.", 5)
    print_wait(f"You find a shiny new {new_stone} energy stone!", 2)
    items.append(new_stone)
    print_wait("It seems so powerful, you ditch your old coal stone "
               "and happily fetch the new one.", 2)
    print_wait("As you walk away, you think, "
               "\"I can't wait to see it light the village!\"", 2)
    get_destination()


def play_game():
    intro()
    get_destination()


def play_again():
    print_wait("Would you like to play again?", 2)
    again = input("Please enter yes or no.\n")
    if "y" in again:
        print_wait("Excellent. Restarting the game.", 2)
        play_game()
    elif "n" in again:
        print_wait("Thank you for playing. Good bye.", 1)
    else:
        print_wait("Sorry, I don't understand.", 1)
        play_again()


play_game()
