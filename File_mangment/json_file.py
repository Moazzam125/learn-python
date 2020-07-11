# JSON | JavaScript Object Notation

import json

json_0 = 'E:\VSCode_Work\Learn_Python\Files\Digits.json'
json_1 = 'E:\VSCode_Work\Learn_Python\Files\greet_user.json'


# Write json

numbers_list = [0,1,2,3,4,5,6,7,8,9]

with open(json_0, 'w') as json_object_0:
    json.dump(numbers_list, json_object_0)

print("\n====================")

username = input("Enter your name:\n>>> ")

with open(json_1, 'w') as json_object_1:
    json.dump(username, json_object_1)


# Read json file

with open(json_0) as json_object_2:
    print(json.load(json_object_2))

print("\n====================")

with open(json_1) as json_object_3:
    username_0 = json.load(json_object_3)
    print("Welcome back, " + username_0.title() + ".")

print("\n====================")