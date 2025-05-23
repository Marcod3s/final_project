import character as ch
import room_1 as r1
import room_2 as r2
import secret_room as sr
import time
# print statements welcoming the user


if __name__ == '__main__':
    username = input("Enter your username: ")
    user = ch.character(username, 35, [])

    print(user)

    r1.stage_1(user)

    r1.stage_2(user)
    print("You've slain the beast of bones")
    sr.secret_encounter(user)

    r2.stage_1(user)

    r2.stage_2(user)

    if "Medallion of Johnny" in user.inventory:
        sr.secret_stage(user)
        print("You have completed the game in it's entirety slaying the secret evil.\n"
          "Congratulations")
    print("You have officially completed the game. Congratulations!")