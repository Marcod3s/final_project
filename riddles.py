import random
import character as ch
import main


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

            if self.answer == user_answer:
                print("Correct!\n Onto the next...")

            else:
                print("Incorrect, try again >:(")
                user_char.add_health(-5)
                print(f"You have {user_char.health} health")
                user_answer = input("What is the answer to my riddle?\n")


all_riddles = [riddle(
    "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by "
    "almost every person. What am I?",
    "Pencil Lead", ch.character),
    riddle(
        "I never was, am always to be, No one ever saw me nor ever will. And yet I am the confidence of "
        "all who live and breath. What am I?",
        "Tomorrow", ch.character),
    riddle("The more you take, the more you leave behind. What am I", "Footsteps", ch.character),
    riddle(
        "I have keys but open no locks. I have space but not room. You can enter, but you can't go "
        "outside. What am I?",
        "A keyboard", ch.character),
    riddle("What comes once in a minute, Twice in a moment, But never in a thousand years?",
           "The letter M", ch.character),
    riddle(
        "The person who makes it, sell it. The person who buys it never uses it, The person who uses it "
        "never knows they're using it. What is it?",
        "A coffin", ch.character)]

np = random.choice(all_riddles)
