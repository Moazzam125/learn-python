# List
        # ln '5' col '10' [] are lists.
        #  '' are must with characters but not with numbers.

bikes = ['honda', 'suzki', 'yamaha', 'toyo', 'super asia', 'unique', ' kawasaki ', 'sohrab']

requested_bikes = ['honda', 'yamaha', 'suzuki' ,'ducati']


# Display the whole list

print(bikes)

print("\n====================")


# Display length of whole list

print( len(bikes) )

print("\n====================")


# Display specfic item in list

print( bikes[0].title() )
print( bikes[-1].title() )

print("\n====================")


# Save a variable from list

message="My first bike was a " + bikes[0].title() + "."

print(message)

print("\n====================")


# Modify list

bikes[1]='suzuki'


# Add items in list

bikes.append('ducati')

print(bikes)

print("\n====================")


# Remove item from list

del bikes[5]

bikes.remove('super asia')

print(bikes)

print("\n====================")


# Hide item from list

bikes.pop()

print(bikes)

print("\n====================")


# Save hidden item in list

popped_bikes = bikes.pop()

print(popped_bikes)

print("\n====================")


# Use of strip

print(bikes[4].strip())
print(bikes[4].rstrip())
print(bikes[4].lstrip())

print("\n====================")


# Use of .sort()

bikes.sort()

print(bikes)

print("========(OR)========")

print(sorted(bikes))

print("\n====================")


# Condition in sort

bikes.sort(reverse = True)

print(bikes)

print("\n====================")


# Use of .reverse()

bikes.reverse()

print(bikes)

print("\n====================")


# Use of .len()

len(bikes)

print(len(bikes))

print("\n====================")


# Slice

print( bikes[:2] )
print( bikes[2:] )
print( bikes[-1:] )
print( bikes[:] )

print("\n====================")


# Loop in list


# Simple

for bike in bikes:
    print(bike.title())
    print(bike.title() + ", is a brand!")

print("\n====================")


# 

for requested_bike in requested_bikes:
    print("prepairing "+ requested_bike.title() + ".")

print("\nFinalizing!")

print("\n====================")


# Single Conditioned list

for requested_bike in requested_bikes:
    if requested_bike == 'ducati':
        print("Sorry, we are out of Ducati.")
    else:
        print("prepairing " + requested_bike.title() + ".")

print("Finalizing!")

print("\n====================")


# Conditioned Multiple lists

for requested_bike in requested_bikes:
    if requested_bike in bikes:
        print("prepairing "+ requested_bike.title() + ".")
    else:
        print("Sorry, we don't have " + requested_bike.title() + ".")

print("\nFinalizing!")

print("\n====================")