import character as ch
def stage_1(character):
    print(f"{character.username} is now in Stage 1")
    input("")

 #Stage 1 is being called

 #Intro
    print("Welcome to Stage 1 of Barrage and Danger, in this stage you must compplete 3 riddles and you will lose health\n each time you grt the answer inccorect.\n Let's see of you make it past the first stage >:)")

    solved = False
    Health = 100

    def riddle ():
        answer = input("xxx").lower()
        return answer == "xxx"

    while not solved:
        if riddle():
            solved = True
            print("You are worthy enough to move on!")
        else: Health = Health - 10
        print(f"You have % {Health} left. ")
    if Health == 0:
        print("You're disqualified")
        exit()
    #First Boss Fight
    print("Now that you have passed this level it is now time to fight your first boss")


def stage_2(character):
    print(f"{character.username}Stage 2 ")

def secret_stage(character):
    print(f"You're not supposed to be here {character.username}")
