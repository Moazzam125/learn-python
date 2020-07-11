# Input
        # using input() store user's input in string.

message = input("Tell me something i will repeat it:\n>>>  ")
print(message)

print("\n====================")


# 

name = input("Enter your name:\n>>>  ")
print("\nAoA,\n" + name + '!')

print("\n====================")


# Using multiple lines in input

prompt = "If you tell us who are you, we can personalize the messages you see."

prompt += "\nWhat is you first name?\n>>> "
            # (+=) operator adds new line to the end of th string.

name_0 = input(prompt)

print("\n AoA," + name_0 + "!")

print("\n====================")


# Numerical compare in input

age = input("How old are you?\n>>> ")

age_0 = int(age)

print(age_0 >= 18)

print("\n====================")


# if statement in input

height = input("How tall are you,in inches?\n>>> ")

height = int(height)

if height >= 36:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll me able to ride when you're little older.")

print("\n====================")


# Modulo

number = input("Enter a number:\n>>> ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

print("\n====================")


# Filling dictionary with input

responses = {}

polling_active = True

while polling_active:
    name = input("Name:\n>>> ")
    response = input("What you want to do:\n>>> ")

    responses[name] = response

    repeat = input("Whould you like to let another person respond? (yes/ no):\n>>> ")

    if repeat == 'no':
        polling_active = False

print("\n\t---Polling Result---\n")

for name, response in responses.items():
    print(name + " want to do " + response + ".")

print("\n====================")