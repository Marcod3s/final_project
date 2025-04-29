import character as ch
import random


def stage_1(character):
    print(f"{character.username} is now in Stage 1")
    input("")

    # Stage 1 is being called

    # Intro
    print(
        "Welcome to Stage 1 of Barrage and Danger, in this stage you must compplete 3 riddles and you will lose health\n each time you grt the answer inccorect.\n Let's see of you make it past the first stage >:)")

    solved = False
    Health = 100

    def riddle():
        answer = input("xxx").lower()
        return answer == "xxx"

    while not solved:
        if riddle():
            solved = True
            print("You are worthy enough to move on!")
        else:
            Health = Health - 10
        print(f"You have % {Health} left. ")
    if Health == 0:
        print("You're disqualified")
        exit()
    # First Boss Fight
    print("Now that you have passed this level it is now time to fight your first boss")


def stage_2(character):
    print(f"{character.username}Stage 2 ")
    print(
        "You have been given a series of attacks listed for you\n Sword attack\n Spin kick\n The force\n Fire ball\n Freeze attack\n You will br given dice to roll. Depending on what number you get determines the amount of damage you will deal.")
    Monster = ch.character("Monster", 50)
    # Insert dice into player's inventory if possible
    Attacks = ["Sword attack", "Spin Kick", "The force", "Fire ball", "Freeze Attack"]
    # Dice_num = random.randint(1, 9)
    #print(f"you did {Dice_num} damage")
    user_choice = input("Choose your attack")

    if user_choice.lower() == "Sword Attack":
        character.add_strikes({Dice_num})
    elif user_choice.lower() == "Spin kick":
        character.add_strikes({Dice_num})
    elif user_choice.lower() == "The force":
        character.add_strikes({Dice_num})
    elif user_choice.lower() == "Fire ball":
        character.add_strikes({Dice_num})
    elif user_choice.lower() == "Freeze attack":
        character.add_strikes({Dice_num})

    #Fight loop starts
    #focus on this for now while loop working and damage being randomized if character rolls even they attack
    turn = 1
    while character.health > 0 and Monster.health > 0:

        print(character.health)
        print(Monster.health)
        #print(f"Turn{turn}")
        u_flag = input("Ready to take your risk?")
        if u_flag.lower == "y" or "yes":
            print("Roll the dice")
            Dice_num = random.randint(1, 9)
            if Dice_num % 2 == 0 :
                Monster.health - {Dice_num}
                print(f"you did {Dice_num} damage")
            else:
                print("Monster countered")
                character.health - {Dice_num}
                print(f"Monster did {Dice_num} damage")





def secret_stage(character):
    print(f"You're not supposed to be here {character.username}")
