import character as ch
import random
import riddles as r


def stage_1(character):
    print(f"{character.username} is now in Room 1, Stage 1")

    # Stage 1 is being called

    # Intro
    print(
        "Welcome to Stage 1 of Barrage and Danger, in this stage you must complete 3 riddles and you will lose "
        "health\n each time you get the answer incorrect."
        "\n Let's see if you make it past the first stage >:)")

    # riddles.np()
    np = random.choice(r.all_riddles)
    print(np)

    user_answer = input("What is the answer to my riddle?")
    np.check_answer(user_answer)

    np = random.choice(r.all_riddles)
    print(np)

    user_answer = input("What is the answer to my riddle?")
    np.check_answer(user_answer)

    np = random.choice(r.all_riddles)
    print(np)

    user_answer = input("What is the answer to my riddle?")
    np.check_answer(user_answer)

    # First Boss Fight
    print("Now that you have passed this level it is now time to fight your first boss")


def stage_2(character):
    print(f"{character.username} is now in Room 1, Stage 2 ")

    monster = ch.character("Beast of Bones", 70, [])

    # Insert dice into player's inventory if possible
    #Attacks = ["1.Sword attack", "2.Spin Kick", "3.The force", "4.Fire ball", "5.Freeze Attack"]

    Dice_atk = random.randint(1, 10)
    # print(f"you did {Dice_num} damage")
    user_choice = input("Choose your attack")

    while character.health < 0 and monster.health < 0:
        dice_roll = random.randint(1, 10)
        if dice_roll % 2 == 0:
            print(
            )
            atk_choice = int(input(
                "You have been given a series of attacks listed for you\n 1.Sword attack\n 2.Spin kick\n 3.The force\n "
                "4.Fire ball\n 5.Freeze attack\n You will br given dice to roll. "
                "Depending on what number you get determines the amount of damage you will deal."))


        else:
            print("Monster attacked you")
            character.health -= {Dice_atk}
            print(f"Monster did {Dice_atk} damage")

        print(character.health)
        print(monster.health)
        # print(f"Turn{turn}")
        u_flag = input("Ready to take your risk?")
        if u_flag.lower == "y" or "yes":
            print("Roll the dice")
            # Dice_num = random.randint(1, 9)

        if user_choice.lower() == "Sword Attack":
            print(f"{character.username} used Sword Attack!\n It Did {Dice_atk} dmg!")
            monster.health -= {Dice_atk}
        elif user_choice.lower() == "Spin kick":
            print(f"{character.username} used Spin Kick!\n It Did {Dice_atk} dmg!")
            monster.health -= {Dice_atk}
        elif user_choice.lower() == "The force":
            print(f"{character.username} used The Force!\n It Did {Dice_atk} dmg!")
            monster.health -= {Dice_atk}
        elif user_choice.lower() == "Fire ball":
            print(f"{character.username} used Fire ball!\n It Did {Dice_atk} dmg!")
            monster.health -= {Dice_atk}
        elif user_choice.lower() == "Freeze attack":
            print(f"{character.username} used Freeze Attack!\n It Did {Dice_atk} dmg!")
            monster.health -= {Dice_atk}

    #Fight loop starts
    # focus on this for now while loop working and damage being randomized if character rolls even they attack
    turn = 1
