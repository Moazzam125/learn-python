# Exceptions | Error message

error_0 = "invalid input"


# try-except Block

try:
    print(5/0)
except ZeroDivisionError:
    print("invalid input")

print("\n====================")


print("\tTwo-numbers division calculator\nPress 'quit' to exit")

while True:
    first_number = input("\nFirst number:\n>>> ")
    if first_number == 'quit':
        break
    second_number = input("\nSecond number:\n>>> ")
    if second_number == 'quit':
        break

    try:
        answer = int(first_number)/int(second_number)
    except TypeError:
        print(error_0)
    except ZeroDivisionError:
        print(error_0)
    except ValueError:
        print(error_0)
    except EOFError:
        print(error_0)
    else:
        print(answer)

print("\n====================")


# Failing Silently

try:
    5/0
except ZeroDivisionError:
    pass

print("\n====================")


# Failing silently in function

def hyper():
    """Hyper"""
    try:
        5/0
    except ZeroDivisionError:
        return None

print("\n====================")