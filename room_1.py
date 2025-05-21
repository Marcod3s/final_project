import character as ch
import random
import riddles as r
import time

def stage_1(character):
    time.sleep(1)
    print(f"{character.username} is now in Room 1, Stage 1")

    # Stage 1 is being called

    # Intro
    time.sleep(1)
    print(
        "Welcome to Stage 1 of Barrage and Danger, in this stage you must complete 3 riddles and you will lose "
        "health\n each time you get the answer incorrect."
        "\n Let's see if you make it past the first stage >:)")

    time.sleep(1)
    np = random.choice(r.all_riddles)
    print(np)
    user_answer = input("What is the answer to my riddle?")
    np.check_answer(user_answer, character)
    r.all_riddles.remove(np)
    print("Correct Answer...")

    time.sleep(1)
    np = random.choice(r.all_riddles)
    print(np)
    user_answer = input("What is the answer to my riddle?")
    np.check_answer(user_answer, character)
    r.all_riddles.remove(np)
    print("Correct Answer...")

    time.sleep(1)
    np = random.choice(r.all_riddles)
    print(np)
    user_answer = input("What is the answer to my riddle?")
    np.check_answer(user_answer, character)
    r.all_riddles.remove(np)
    print("Correct Answer...")

    # First Boss Fight
    time.sleep(1)
    print("Now that you have passed this level it is now time to fight your first boss")


def stage_2(character):
    time.sleep(1)
    print(f"{character.username} is now in Room 1, Stage 2 ")

    monster = ch.character("Beast of Bones", 70, )
    time.sleep(1)
    print(f"There is a boss in this stage\n {monster}")
    time.sleep(2)
    print("Because this is your first boss fight let me teach you how things go..\n\n"
          "There is a 1 in 2 chance you get to attack\n")
    time.sleep(2)
    print("Furthermore, because you're new here your attacks "
          "have randomized damage value from 5dmg-10dmg for now")
    time.sleep(2)
    print("Depending on what number you get determines the amount of damage you will deal.")
    # print(f"you did {Dice_num} damage")

    # Fight loop starts

    while character.health > 0 and monster.health > 0:
        if character.health <= 0:
            print("Game over...")
            exit()
        dice_atk = random.randint(5, 10)
        dice_roll = random.randint(1, 10)
        if dice_roll % 2 == 0:
            print(f"The Beast of Bones currently has {monster.health} health")
            time.sleep(1)
            print("It's currently now your turn")
            time.sleep(1)
            print(
                "You have been given a series of attacks listed for you\n "
                "1.Sword Attack\n"
                "2.Spin Kick\n"
                "3.The Force\n"
                "4.Fire Ball\n"
                "5.Freeze Attack\n")

            atk_choice = input("Choose your attack")
            if atk_choice == 1 or atk_choice == "Sword Attack":
                time.sleep(1)
                print(f"{character.username} used Sword Attack!\n It Did {dice_atk} dmg!")
                monster.add_health(-dice_atk)

            elif atk_choice == 2 or atk_choice == "Spin Kick":
                time.sleep(1)
                print(f"{character.username} used Spin Kick!\n It Did {dice_atk} dmg!")
                monster.add_health(-dice_atk)

            elif atk_choice == 3 or atk_choice == "The Force":
                time.sleep(1)
                print(f"{character.username} used The Force!\n It Did {dice_atk} dmg!")
                monster.add_health(-dice_atk)

            elif atk_choice == 4 or atk_choice == "Fire Ball":
                time.sleep(1)
                print(f"{character.username} used Fire ball!\n It Did {dice_atk} dmg!")
                monster.add_health(-dice_atk)

            elif atk_choice == 5 or "Freeze Attack":
                time.sleep(1)
                print(f"{character.username} used Freeze Attack!\n It Did {dice_atk} dmg!")
                monster.add_health(-dice_atk)

            else:
                time.sleep(1)
                print(f"{character.username} did something wrong and "
                      f"forfeited their chance at an attack.")
                return
        else:
            print("The Beast of Bones attacked you")
            time.sleep(1)
            character.add_health(-dice_atk/2)
            time.sleep(2)
            print(f"The Beast of Bones did {dice_atk / 2} damage! \n")
            time.sleep(1)
            print(f"you now have {character.health} health")
