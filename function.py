# Function


# Define a function

def greet():
    """Display a simple greeting"""
    print("Python")

greet()

print("\n====================")


# Passing Info to function

def greet_user(username):
    """Display a simple greeting"""
    print("AoA, " + username.title() + "!")

greet_user('Moazzam')

print("\n====================")


# Positional Arguments

def pets(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

pets('cat', 'black cat')

print("\n====================")


# Default values

def my_pets(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

my_pets('black dog')

print("\n====================")


# Keyword Arguments

my_pets(pet_name = 'black dog')

print("\n====================")


# Return Values in variables

def formatted_name(first_name, last_name):
    """Dislay full name, neatly"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

print(formatted_name('moazzam', 'muhammad'))

print("\n====================")


# Save it as a variable

person_2 = formatted_name('moazzam', 'muhammad')

print(person_2)

print("\n====================")


# Making arguments optional

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

person_1 = get_formatted_name('hafiz', 'muhammd', 'uzair')
person_2 = get_formatted_name('moazzam', 'muhammad')

print(person_1)
print(person_2)

print("\n====================")


# Using Tuple
                # (*) is a tuple.

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + " -inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(20, 'pepperoni')
make_pizza(25, 'pepperoni', 'extra cheese')

print("\n====================")


# Returning a Dictionanry

def build_person(first_name, last_name):
    """Display information about a person"""
    person_3 = {'first': first_name, 'last': last_name}
    return person_3

print(build_person('moazzam', 'muhammad'))

print("\n====================")


# Work with multiple values

def person_name_age(first_name, last_name, age=''):
    """Dislplay information first name, last name & age"""
    person_5 = {'first': first_name, 'last': last_name}

    if age:
        person_5['age'] = age
    
    return person_5

print(person_name_age('moazzam', 'muhammad', 16))

print("\n====================")


# Artributry Keyword arguments


def build_profile(first, last, **user_info):
    """Build a dictionary contains everything about a user"""
    profile = {}
    profile['first'] = first
    profile['last'] = last
    
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

profile = build_profile('Moazzam', 'Muhammad',
location = 'gujranwala',
field = 'Programming')

print(profile)

print("\n====================")


# Loop


# for loops in function

def greet_users(names):
    """Display greeting to each user in list"""
    for name in names:
        print("AoA, " + name.title() + "!")

usernames = ['moazzam', 'muzammyl']
greet_users(usernames)

print("\n====================")


# Modifing list in function

def print_models(unprinted_models, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to comleted_models after printing.
    """
    while unprinted_models:
        current_design = unprinted_models.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were completed."""
    print("\nThe following models have been completed:")

    for completed_model in completed_models:
        print(completed_model)
    
unprinted_models = ['iphone case', 'robot pendant', 'ducati model']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)

print("\n====================")


# While loops in function | list in function

active = True

while active:
    print("Tell me your name")
    f_name = input("First name:\n>>> ")
    l_name = input("Last name:\n>>> ")

    get = formatted_name(f_name, l_name)
    print("AoA, " + get + "!")

    exiting = input("Would you like to close it? (yes/ no)\n>>> ")

    if exiting == 'yes':
        active = False

print("\n====================")