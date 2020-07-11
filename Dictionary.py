# Dictionary
                # Brackets {} of ln '6' shows the dictionary.
                # The text in Colomn '12' of ln '6' is the heading by sign (:)
                # Next to the heading will be the material.

browser_0 = {'name': 'firefox', 'company': 'mozilla', 'version': 'esr', 'type': 'content blocker', 'store': 'addons', 'speed': 'high'}


# List

aliens = []


# Second method of dictionary

browser_1 = {
    'name': 'chrome',
    'company': 'Google',
    'version': 'Dev',
    'type': 'Stylist',
    'store': 'webstore',
    'speed': 'slow',
}



# Display method of dictionary

print( browser_0['company'].title() + " " + browser_0['name'].title() + " " +browser_0['version'].upper())

print("\n====================")


# Make variables from dictionary

full_name_browser_0 = browser_0['company'].title() + " " + browser_0['name'].title() + " " +browser_0['version'].upper()

print("My browser_0 is " + str(full_name_browser_0) + ".")

print("\n====================")

# Nesting


# Dictionary in dictionary

users = {
    'moazzam125': {
        'first': 'moazzam',
        'last': 'muhammad',
        'location': 'gujranwala, pakistan',
    },
    'muzammyl_75': {
        'first': 'muzammyl',
        'last': 'muhammad',
        'location': 'gujranwala, pakistan',
    },
}


# List in dictonary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}


# Make veraible from nest


# dictionary in dictionary



# Add items to Dictionary

print(browser_0)

browser_0['theme'] = 'light'
browser_0['upload'] = 0.902
browser_0['download'] = 25

print(browser_0)

print("\n====================")


# Modify the existing item

print("My browser_0's default theme is " + browser_0['theme'].title() + ".")

browser_0['theme'] = 'dark'

print("I changed my browser_0's theme to " + browser_0['theme'].title() + ".")

print("\n====================")


print("Original upload speed is: " + str(browser_0['upload']))

if browser_0['speed'] == 'slow':
    acceleration = 1
elif browser_0['speed'] == 'medium':
    acceleration = 2
else:
    acceleration = 3

browser_0['upload'] = browser_0['upload'] + acceleration

print("New upload speed is: " + str(browser_0['upload']))

print("\n====================")


# Adding dictionary

print(browser_0, browser_1)

print("\n====================")


print(browser_0, "\n", browser_1) 

print("\n====================")


# Make variable from added dictionaries

firf_vs_chrm = [browser_0, browser_1]

print(firf_vs_chrm)

print("\n====================")


# Remove item

del browser_0['store']
print(browser_0)

print("\n====================")


# Use of .items()

print(browser_1.items())

print("\n====================")


# Use of .keys()

print(browser_1.keys())

print("\n====================")


# Use of .values()

print(browser_1.values())

print("\n====================")

# Loop in dictionary


# Loop in dictionary


# Loop through Added dictionaries

for browser_compare in firf_vs_chrm:
    print(browser_compare)

print("\n====================")


for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")

print("\n====================")

# Conditional Loop

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'
    else:
        alien['color'] = 'brown'
        alien['speed'] = 'extrme'
        alien['points'] = '20'

for alien in aliens[:5]:
    print(alien)

print("...")

print("The total numbers of aliens: " + str(len(aliens)))

print("\n====================")


# Loop through .items()

for key, value in browser_1.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("\n====================")


# Loop through .keys()

for name in browser_1.keys():
    print(name.title())

print("\n====================")


# Loop through .values()

for name in browser_1.values():
    print(name.title())

print("\n====================")


# Loop through nest


# Loop through dictionary in dictionary

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

print("\n====================")


# Loop through list in dictionary

print("You ordered a " + pizza['crust'] + "-crust pizza with following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

print("\n====================")