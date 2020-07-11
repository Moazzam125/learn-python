# Text | .txt

txt_0 = 'E:\VSCode_Work\Learn_Python\Files\Digits_file.txt'
txt_1 = 'E:\VSCode_Work\Learn_Python\Files\Digits.txt'
txt_2 = 'E:\VSCode_Work\Learn_Python\Files\Write_Empty.txt'

# Read file from current directary


# Read file with abolute file path
                                    # In windows mentions local disk.
                                    # The open() function automatically creates the file.

with open('E:\VSCode_Work\Learn_Python\Files\Digits_file.txt') as txt_object_0:
    contents_0 = txt_object_0.read()
    print(contents_0)

print("\n====================")


# Read line by line file

with open(txt_0) as txt_object_1:
    for line_0 in txt_object_1:
        print(line_0)

print("\n====================")

with open(txt_0) as txt_object_2:
    for striped_text in txt_object_2:
        print(striped_text.strip())

print("\n====================")


# Create List from lines

txt_list_3 = ''
with open(txt_2) as txt_object_3:
    lines_0 = txt_object_3.readlines()

    for line_1 in lines_0:
        print(line_1.rstrip())
        
        
        # List preview
    
        print(line_1[:].rstrip())

print("\n====================")


# Work with file contents


# Writing data to empty file
                                # (file, 'w') the 'w'write, 'r'read, 'a'append, 'r+' OR 'w+'read & write
                            

with open(txt_2, 'w') as txt_object_4:
    txt_object_4.write("\tKeyboard\n")
    txt_object_4.write("1234567890-=qwertyuiop[]asdfghjkl;'\zxcvbnm,./`")
    print(txt_object_4)

print("\n====================")


# Appending in existing file
                                # python will create file if not exist

with open(txt_2, 'a') as txt_object_5:
    txt_object_5.write("\n~!@# $%^&*()_+QWERTYUIOP{}ASDFGHJKL:""|ZXCVBNM<>?")

# Copy to string

txt_list_0 = ''

with open(txt_0) as txt_object_5:
    lines_1 = txt_object_5.readlines()

    for line_2 in line_1:
        txt_list_0 += line_2.strip()

    print(txt_list_0)
    print(len(txt_list_0))

print("\n====================")


# Use of .split()
# Build list of words from string

txt_3 = input("\tFile Explorer\nEnter 'quit' to exit\nEnter a file path:\n>>> ")

while True:
    if txt_3 == 'quit':
        False
    try:
        with open(txt_3, 'r') as txt_object_6:
            contents_1 = txt_object_6.read()
    except FileNotFoundError:
        print("File not found")
        break
    except FileNotFoundError:
        print("invalid input")
        break
    else:
        characters = len(contents_1)
        words = contents_1.split()
        number_of_words = len(words)
        print("The file has number of characters " + str(characters) + " and " + str(number_of_words) + " number of words.")
        break

print("\n====================")


# Test with file

txt_list_1 = ''

with open(txt_1) as txt_object_7:
    lines_2 = txt_object_7.readlines()

    for line_3 in lines_2:
        txt_list_1 += line_3

birthday = input("choose (100/1000):\n>>> ")

if birthday in txt_list_1:
    print("You typed 100!")
else:
    print("You typed above 100!")

print("\n====================")


# Work with lists

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['E:\VSCode_Work\Learn_Python\Files\Digits_file.txt', 'E:\VSCode_Work\Learn_Python\Files\Write_Empty.txt']
for filename in filenames:
    count_words(filename)

print("\n====================")