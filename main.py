import character as ch, room_1 as r1,room_2 as r2, secret_room as sr

char_classes = {
    'Barbarian': [150, (['sword', 10], ['mead', 20])],
    'Mage': [110, ('wand', 'potion')]
}

#print statements welcoming the user

username = input("Enter your username: ")
user_pick = input("what class do you want to be?")

main_character = ch.character(username, char_classes[user_pick][0], char_classes[user_pick][1], user_pick)

for char_class in char_classes:
    if char_class == user_pick:
        user_character = ch.character('test', char_classes[user_pick][0], char_classes[user_pick][1], user_pick)

print(main_character)


# user_class = False
# #while not user_class:
#         #print(f"Now you must pick a class {c.username}")
# #character = ch.character(username, 10) #placeholder)
# #beginning the game
#
#
r1.stage_1(ch.character)
r1.stage_2(ch.character)
r2.stage_1(ch.character)
r2.stage_2(ch.character)


