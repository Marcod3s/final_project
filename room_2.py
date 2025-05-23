import character as ch
import riddles as r
import random
import time

def stage_1(character):
    print(f"{character.username} is currently in room 2, stage 1")
    time.sleep(1)
    character.health = 45
    print(f"For purposes of ease your health will be metastasized to {character.health}")
    character.health = 45
    time.sleep(1)
    print("So you've slain your first boss huh? You must think your hot stuff. We'll see how you fare...")

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

def stage_2(character):
    print(f"{character.username} is currently in room 2, stage 2")
    monster2 = ch.character("Rick soldier of God", 150, [])
    print(f"There is a boss in this stage {monster2}")

    while character.health > 0 and monster2.health > 0:
        if character.health <= 0:
            print("Game over...")
            exit()
        dice_atk = random.randint(12, 25)
        dice_roll = random.randint(1, 10)
        if dice_roll % 2 == 0:
            print(f"{monster2.username} currently has {monster2.health} health")
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
            if atk_choice == "1" or atk_choice == "Sword Attack":
                time.sleep(1)
                print(f"{character.username} used Sword Attack!\n It Did {dice_atk} dmg!")
                monster2.add_health(-dice_atk)

            elif atk_choice == "2" or atk_choice == "Spin Kick":
                time.sleep(1)
                print(f"{character.username} used Spin Kick!\n It Did {dice_atk} dmg!")
                monster2.add_health(-dice_atk)

            elif atk_choice == "3" or atk_choice == "The Force":
                time.sleep(1)
                print(f"{character.username} used The Force!\n It Did {dice_atk} dmg!")
                monster2.add_health(-dice_atk)

            elif atk_choice == "4" or atk_choice == "Fire Ball":
                time.sleep(1)
                print(f"{character.username} used Fire ball!\n It Did {dice_atk} dmg!")
                monster2.add_health(-dice_atk)

            elif atk_choice == "5" or atk_choice == "Freeze Attack":
                time.sleep(1)
                print(f"{character.username} used Freeze Attack!\n It Did {dice_atk} dmg!")
                monster2.add_health(-dice_atk)

            else:
                time.sleep(1)
                print(f"{character.username} did something wrong and "
                      f"forfeited their chance at an attack.")
        else:
            print(f"{monster2.username} attacked you")
            time.sleep(1)
            character.add_health(-dice_atk / 3)
            time.sleep(2)
            print(f"{monster2.username} did {dice_atk / 3} damage! \n")
            time.sleep(1)
            print(f"you now have {character.health} health")
            if character.health <= 0:
                print("Game over...")
                exit()
            elif monster2.health <= 0:
                print(f"You've slain {monster2.username}")

    print("You have beaten this dungeon\n Congratulations!")