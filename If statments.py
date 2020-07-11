# If Statments

# 'if' is a conditional statment.

cars=['audi','suzuki','bmw','toyota']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']

# Equalliy

print(cars[0] == 'audi')
print(cars[0] == 'Audi')
print(cars[0].title() == 'Audi')

print("\n====================")


print(numbers[17] == '18')

print("\n====================")


# Inequallity
                # (!=) shows it is not equal to.

if cars[0] != 'suzuki':
    print(cars[1] == 'suzuki')

print("\n====================")


if numbers[16] != '42':
    print("Incorrect statment")

print("\n====================")


# Compare

print(numbers[15] < '21')
print(numbers[15] <= '15')
print(numbers[15] > '14')
print(numbers[15] >= '17')

print("\n====================")


# Comparing multiple values
                            # 'and' means both should be true.
                            # 'or' means one should be true.

print(numbers[17] >= '17') and (numbers[21] >= '21')    
print(numbers[17] >= '17') or (numbers[21] == '21')
print(numbers[15] >= '19') and (numbers[21] >= '21')
print(numbers[16] == '18') or (numbers[21] == '21')

print("\n====================")


# Multiple if condition 

if 'audi' in cars:
    print("prepairing Audi")
if 'suzuki' in cars:
    print("prepairing suzuki")

print("\nFinalizing!")

print("\n====================")


# if-else chain
                    # ln '' if condition that pass to be performed.
                    # ln '' else perform its fuction when condition results in fails.

if numbers[17] <= '18':
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote!")

print("\n====================")


# if-elif chain

if numbers[11] < '4':
    price = 0
elif numbers[17] < '18':
    price = 5
elif numbers[21] < '22':
    price = 10

print("Your admission fee is $" + str(price)+".")

print("\n====================")


# if-elif-else chain

if numbers[17] <= '4':
    print("Your admission fee is $0.")
elif numbers[17] <= '18':
    print("Your admission fee is $5.")
else:
    print("Your admission fee is $10.")

print("\n====================")


if numbers[11] < '4':
    price = 0
elif numbers[11] < '18':
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

print("\n====================")


if numbers[11] < '4':
    price = 0
elif numbers[17] <'18':
    price = 5
elif numbers[24] < '22':
    price = 10
else:
    price = 15

print("Your admission fee is $" + str(price)+".")

print("\n====================")


if 'audi' in cars:
    print("prepairing Audi")
elif 'suzuki' in cars:
    print("prepairing suzuki")
elif 'yamaha' in cars:
    print("prepairing yamaha")
else:
    print("Sorry, nothing could be prepaired!")

print("\nFinalizing!")

print("\n====================")


# Loop in if statments


# Loop for .upper()

for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())

print("\n====================")