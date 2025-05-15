import random


class riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return self.question

    def check_answer(self, user_answer, ):
        while user_answer != self.answer:

            if self.answer == user_answer:
                print("Correct!\n Good Job!")
            else:
                print("Incorrect")


# np = riddle("What is black and white and read all over?", "A newspaper")

all_riddles = [riddle(
    "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by "
    "almost every person. What am I?",
    "Pencil Lead"),
    riddle(
        "I never was, am always to be, No one ever saw me nor ever will. And yet I am the confidence of "
        "all who live and breath. What am I?",
        "Tomorrow"),
    riddle("The more you take, the more you leave behind. What am I", "Footsteps"),
    riddle(
        "I have keys but open no locks. I have space but not room. You can enter, but you can't go "
        "outside. What am I?",
        "A keyboard"),
    riddle("What comes once in a minute, Twice in a moment, But never in a thousand years?",
           "The letter M"),
    riddle(
        "The person who makes it, sell it. The person who buys it never uses it, The person who uses it "
        "never knows they're using it. What is it?",
        "A coffin")]

np = random.choice(all_riddles)
print(np)
user_answer = input("What is the answer to my riddle?")
np.check_answer(user_answer)
