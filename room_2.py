import character as ch
import riddles as r
import random
import time

def stage_1(character):
    print(f"{character.username} is currently in room 2, stage 1")
    print("So you've slain your first boss huh? You must think your hot stuff. We'll see how you fare...")

    np = random.choice(r.all_riddles)
    print(np)
    user_answer = input("What is the answer to my riddle?")
    np.check_answer(user_answer, character)
    r.all_riddles.remove(np)

    np = random.choice(r.all_riddles)
    print(np)
    user_answer = input("What is the answer to my riddle?")
    np.check_answer(user_answer, character)
    r.all_riddles.remove(np)

    np = random.choice(r.all_riddles)
    print(np)
    user_answer = input("What is the answer to my riddle?")
    np.check_answer(user_answer, character)
    r.all_riddles.remove(np)

def stage_2(character):
    print(f"{character.username} is currently in room 2, stage 2")
    monster2 = ch.character("Rick soldier of God", 150, )
    print(f"There is a boss in this stage {monster2}")

    while character.health > 0 and monster2.health > 0:
        print("Depending on what number you get determines the amount of damage you will deal.")
        dice_atk = random.randint(12, 25)
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
                monster2.add_health(-dice_atk)
                print(f"The Beast of Bones currently has {monster2.health} health")
            elif atk_choice == 2:
                print(f"{character.username} used Spin Kick!\n It Did {dice_atk} dmg!")
                monster2.add_health(-dice_atk)
                print(f"The Beast of Bones currently has {monster2.health} health")
            elif atk_choice == 3:
                print(f"{character.username} used The Force!\n It Did {dice_atk} dmg!")
                monster2.add_health(-dice_atk)
                print(f"The Beast of Bones currently has {monster2.health} health")
            elif atk_choice == 4:
                print(f"{character.username} used Fire ball!\n It Did {dice_atk} dmg!")
                monster2.add_health(-dice_atk)
                print(f"The Beast of Bones currently has {monster2.health} health")
            elif atk_choice == 5:
                print(f"{character.username} used Freeze Attack!\n It Did {dice_atk} dmg!")
                monster2.add_health(-dice_atk)
                print(f"The Beast of Bones currently has {monster2.health} health")

        else:
            print("The Beast of Bones attacked you")
            character.add_health(dice_atk / 2)
            print(f"The Beast of Bones did {-dice_atk / 2} damage! \n"
                  f"you now have {character.health} health")
