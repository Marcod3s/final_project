import riddles as r
import character as ch
import time
import random

def secret_encounter(character):
    print("Hola mi amigo\n"
          "My name's Johnny ")
    time.sleep(1)
    journey_choice = input("I uh was wondering if you need help on your journey?\n"
                           "You may either punch Johnny or decline his offer")
    if (journey_choice == "punch" or journey_choice == "P"
            or journey_choice == "Punch" or journey_choice == "p"):
        print("You killed Johnny with one punch.\n"
              "Are you proud of yourself?")
        character.add_inventory("Medallion of Johnny")
    else:
        print("Johnny: Aw man welp I guess I'll see you later")
def secret_stage(character):
    time.sleep(1)
    print(f"You're not supposed to be here {character.username}")
    time.sleep(1)
    print("You were never supposed to see me like this")
    time.sleep(1)
    print("I was the one in charge of the riddles all this time")
    time.sleep(1)
    print("If you can solve these as well you may have a chance to defeat me")


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


    sr_monster = ch.character("ynnhoJ", 250, [])
    print(f"There is a boss in this stage {sr_monster}")

    while character.health > 0 and sr_monster.health > 0:
        if character.health <= 0:
            print("Game over...")
            exit()
        dice_atk = random.randint(25, 30)
        dice_roll = random.randint(1, 10)
        if dice_roll % 2 == 0:
            print(f"ynnhoJ currently has {sr_monster.health} health")
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
                sr_monster.add_health(-dice_atk)

            elif atk_choice == "2" or atk_choice == "Spin Kick":
                time.sleep(1)
                print(f"{character.username} used Spin Kick!\n It Did {dice_atk} dmg!")
                sr_monster.add_health(-dice_atk)

            elif atk_choice == "3" or atk_choice == "The Force":
                time.sleep(1)
                print(f"{character.username} used The Force!\n It Did {dice_atk} dmg!")
                sr_monster.add_health(-dice_atk)

            elif atk_choice == "4" or atk_choice == "Fire Ball":
                time.sleep(1)
                print(f"{character.username} used Fire ball!\n It Did {dice_atk} dmg!")
                sr_monster.add_health(-dice_atk)

            elif atk_choice == "5" or atk_choice == "Freeze Attack":
                time.sleep(1)
                print(f"{character.username} used Freeze Attack!\n It Did {dice_atk} dmg!")
                sr_monster.add_health(-dice_atk)

            else:
                time.sleep(1)
                print(f"{character.username} did something wrong and "
                      f"forfeited their chance at an attack.")
        else:
            print(f"{sr_monster} attacked you")
            time.sleep(1)
            character.add_health(-dice_atk / 3)
            time.sleep(2)
            print(f"{sr_monster.username} did {dice_atk / 3} damage! \n")
            time.sleep(1)
            print(f"you now have {character.health} health")
            if character.health <= 0:
                print("Game over...")
                exit()
            elif sr_monster.health <= 0:
                print(f"You have slain {sr_monster.username}")
