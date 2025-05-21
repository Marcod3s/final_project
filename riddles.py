import random
import character as ch
import time


class riddle:
    def __init__(self, question, answer, user_char):
        self.question = question
        self.answer = answer
        self.user_char = ch.character
        ch.character = user_char

    def __str__(self):
        return self.question

    def check_answer(self, user_answer, user_char):
        while user_answer != self.answer:

            if self.answer == user_answer.lower() or self.answer == user_answer:
                time.sleep(1)
                return user_answer.lower()
            else:
                print("Incorrect, try again >:(")
                user_char.add_health(-5)
                time.sleep(1)
                print(f"You have {user_char.health} health")
                if user_char.health <= 0:
                    print("Game over...")
                    exit()
                user_answer = input("What is the answer to my riddle?\n")
        return None


all_riddles = [riddle(
    "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by "
    "almost every person. What am I?",
    "pencil lead", ch.character),
    riddle(
        "I never was, am always to be, No one ever saw me nor ever will. And yet I am the confidence of "
        "all who live and breath. What am I?",
        "tomorrow", ch.character),
    riddle("The more you take, the more you leave behind. What am I", "footsteps", ch.character),
    riddle(
        "I have keys but open no locks. I have space but not room. You can enter, but you can't go "
        "outside. What am I?",
        "a keyboard", ch.character),
    riddle("What comes once in a minute, Twice in a moment, But never in a thousand years?",
           "the letter m", ch.character),
    riddle(
        "The person who makes it, sell it. The person who buys it never uses it, The person who uses it "
        "never knows they're using it. What is it?",
        "a coffin", ch.character)]

np = random.choice(all_riddles)

