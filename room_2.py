import character as ch
import riddles as r
import random


def stage_1(character):
    print(f"{character.username} is currently in room 2, stage 1")
    print("So you've slain your first boss huh? You must think your hot stuff. We'll see how you fare...")
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


def stage_2(character):
    print(f"{character.username} is currently in room 2, stage 2")
