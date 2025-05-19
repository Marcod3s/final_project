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

    monster = ch.character("Beast of Bones", 70,)
    print(f"There is a boss in this stage {monster}")
    print("Because this is your first boss fight let me teach you how things go..\n"
          "There is a 1 in 2 chance you get to attack\n"
          "Furthermore because you're new here your attacks have randomized damage value from 5dmg-10dmg")
    # print(f"you did {Dice_num} damage")

    # Fight loop starts

    while character.health > 0 and monster.health > 0:
        print("Depending on what number you get determines the amount of damage you will deal.")
        dice_atk = random.randint(5, 10)
        dice_roll = random.randint(1, 10)
        if dice_roll % 2 == 0:
            print("It's currently now your turn")
            print(
                  "You have been given a series of attacks listed for you\n "
                  "1.Sword attack\n"
                  "2.Spin kick\n "
                  "3.The force\n"
                  "4.Fire ball\n "
                  "5.Freeze attack\n ")

            atk_choice = int(input("Choose your attack"))
            if atk_choice == 1:
                print(f"{character.username} used Sword Attack!\n It Did {dice_atk} dmg!")
                monster.health -= dice_atk
                print(f"The Beast of Bones currently has {monster.health} health")
            elif atk_choice == 2:
                print(f"{character.username} used Spin Kick!\n It Did {dice_atk} dmg!")
                monster.health -= dice_atk
                print(f"The Beast of Bones currently has {monster.health} health")
            elif atk_choice == 3:
                print(f"{character.username} used The Force!\n It Did {dice_atk} dmg!")
                monster.health -= dice_atk
                print(f"The Beast of Bones currently has {monster.health} health")
            elif atk_choice == 4:
                print(f"{character.username} used Fire ball!\n It Did {dice_atk} dmg!")
                monster.health -= dice_atk
                print(f"The Beast of Bones currently has {monster.health} health")
            elif atk_choice == 5:
                print(f"{character.username} used Freeze Attack!\n It Did {dice_atk} dmg!")
                monster.health -= dice_atk
                print(f"The Beast of Bones currently has {monster.health} health")

        else:
            print("The Beast of Bones attacked you")
            character.health -= dice_atk/2
            print(f"The Beast of Bones did {dice_atk/2} damage! \n"
                  f"you now have {character.health} health")


