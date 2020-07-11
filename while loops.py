# While loop
            # Continous loop

current_number = 6


while current_number <= 5:
    print(current_number)

print("\n====================")


# Count

while current_number <= 10:
    print(current_number)
    current_number += 1

print("\n====================")

prompt = "\nEnter 'quit' to exit:\n>>> "

message = ""

while message != 'quit':
    message = input(prompt)

print("\n====================")


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nDon't say 'quit'!\n>>> "

active = True

while active:
    message = input(prompt)
    
    if message != 'quit':
        active = False
    elif message != 'moazzam':
        active = False
    else:
        print(message)

print("\n====================")


# Breaking method
                    # A loop with True will end only on break statment.

while True:
    prompt = "Tell me a name of city:\nType 'quit' to exit:\n>>> "
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd like to go to " + city.title() + "!")

print("\n====================")


# Continue method

number = input("Write a number\n>>> ")

active_0 = True

while active_0: 

    if number == 0:
        continue
        active_0 = False
    else:
        print(number)
        active_0 = False

print("\n====================")


# Avoiding Infinite Loop

x = 1

while x <= 5:
    print(x)
    x += 1

print("\n====================")


# While loops in list


# Moving one item from one list to another list

unconfirmed_users = ['moazzam', 'muzammyl', 'talha']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifing user: " + current_user.title() + ".")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")

for confirmed_users in confirmed_users:
    print(confirmed_users.title())

print("\n====================")


# Remove all items with same name from list

pets = ['dog', 'cat', 'cat', 'cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

print("\n====================")