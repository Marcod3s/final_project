# char_classes = {
#     'Barbarian': [150, ('sword', 'mead')],
#     'Mage': [110, ('wand', 'potion')]
# }
#
# print(char_classes['Barbarian'][1])

class riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return self.question

    def check_answer(self, user_answer):
        if self.answer == user_answer:
            print("Correct!")
        else:
            print("Incorrect")


np = riddle("What is black and white and read all over?", "A newspaper")
all_riddles =[riddle("What is black and white and read all over?", "A newspaper"), riddle("Who is the best teacher at loughlin?", "Mr. Bartnikowski")]

import random
np = random.choice(all_riddles)
print(np)
user_answer = input("What is the answer to my riddle?")
np.check_answer(user_answer)