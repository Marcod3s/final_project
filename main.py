import character as ch




# print statements welcoming the user

username = input("Enter your username: ")
character = ch.character(username, 30, [])

print(character)

import room_1 as r1

r1.stage_1(character)

r1.stage_2(character)

import room_2 as r2

r2.stage_1(character)

r2.stage_2(character)
