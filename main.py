import character as ch
import room_1 as r1
import room_2 as r2
import random
import riddles as r

# print statements welcoming the user


if __name__ == '__main__':
    username = input("Enter your username: ")
    user = ch.character(username, 30,)

    print(user)

    r1.stage_1(user)

    r1.stage_2(user)

    r2.stage_1(user)

    r2.stage_2(user)
