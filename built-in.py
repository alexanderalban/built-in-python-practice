# Practicing using the functions built into Python

# The abs function returns the absolute value of a number without it's sign (10 is 10, -10 is also 10). say you're counting how many steps a character
# was taking in a game. this would allow both forward and backward steps to be counted

from copy import copy
from shutil import copyfile, copytree


print(abs(-10))

steps = -3
if abs(steps) > 0:
    print("Character is moving")

# The Bool function. Short for boolean, true or false

print(bool(0))
print(bool(1))

print(bool(None))
print(bool(' '))
print(bool("Hello"))

# The dir function, short for directory, returns information about any value

print(dir(['a', 'short', 'list']))
print(dir(1))

popcorn = 'I love popcorn!'
print(dir(popcorn))

help(popcorn.upper)

# Eval, short for evaluate. Takes a string as a parameter and runs it as though it were a Python expression

# your_calculation = input('Enter a calculation')
# result = eval(your_calculation)
# print(result)

# The exec function is like eval, but does not return a value. Can be used to run more complicated programs

my_small_program = '''print('ham')
print('sandwich')'''

exec(my_small_program)

# The float function, turns an integer (10, 34, etc) into a floating point number (10.0, 34.0, etc)

print(float('12'))

#Int turns an integer or string into a whole number

print(int(123.45))
print(int('456'))

# A string containing a floating point number doens't work. It's confusing
# print(int('123.456'))

# The Len Function, short for length. Returns the length of an object or, in the case of a string, returns the number of characters in the string

print(len("This is just a test string"))

power_ranger_list = ["Jason", "Tommy", "Kimberly", "Trini", "Zack", "Billy"]
print(len(power_ranger_list))

enemy_map = {'Batman' : 'Joker',
    'Superman' : 'Lex Luthor',
    'Wonder Woman' : 'Cheetah',
    "Green Lantern" : 'Sinestro',
    'Flash' : 'Captain Cold'}

print(len(enemy_map))

# Particularly helpful in loops

fruit = ['apple', 'banana', 'clementine', 'dragon fruit']
length = len(fruit)

for x in range(0, length):
    print('the fruit at index %s is %s' % (x, fruit[x]))

# Max and Min functions. Max returns the largest item in a list, tuple, or string. 

numbers = [5, 4, 10, 27, 3]
print(max(numbers))

print(max(10, 300, 450, 50, 90))

# Min works like max, but returns the smallest

smallnums = [5, 4, 10, 30, 22]
print(min(smallnums))

# Guessing game where if you guess above the chosen number, all players lose, but if they are all below, all players win. Kind of group Price is Right rules

guess_this_number = 61
player_guesses = [12, 15, 70, 45]
if max(player_guesses) > guess_this_number:
    print('Boom! You all lose.')
else: print('You win!')

# The Range Function. Mainly used for loops, to loop through a section of code a specific number of times. The paramaters are start and stop. The stop is one less
# than the second parameter, as code begins at position 0

for x in range(0, 5):
    print(x)

# Range returns a special object called an iterator that repeats an action a number of times. 
# Can convert the iterator into a list using the list function

print(list(range(0, 5)))

# Can add a third parameter for range called step. The number 1 is used by default if no step is specified.

count_by_twos = list(range(0, 30, 2))
print(count_by_twos)

# You can also use negative steps
count_down_by_twos = list(range(40, 10, -2))
print(count_down_by_twos)

# The Sum function adds items in a list and returns the total

add_numbers = list(range(0, 500, 50))
print(add_numbers)
print(sum(add_numbers))

# Working with files! Let's create a file in notepad and open it using python.

test_file = open('d:\\code\\python-practice\\test-python.txt')
text = test_file.read()
print(text)

# Writing to files. We can create a new, empty file by using a second parameter: the string 'w' 

# test_file = open('d:\\code\\python-practice\\mynewshineyfile.txt', 'w')

# Now we write into the file directly

# test_file.write('This is a test file! I did it!')
# test_file.close

##### More Practice!

# Run this code and see what happens

a = abs(10) + abs(-10)
print(a)

b = abs(-10) + -10
print(b)

# A hidden message. try using dir and help to find out how to break a string into words, and then create a small program to print every other word
# in the following string, starting with the word (this)

hidden = "this if is you not are a reading very this good then way you to have hide done a it message wrong"

print(dir(hidden))
# help(hidden.split)

revealed = hidden.split()
print(revealed)

for x in range(0, len(revealed), 2):
    print(revealed[x])

# Create a program to copy a file

copytest = open('d:\\code\\python-practice\\built-in-python-practice\\copytest.txt', 'w')
copytest.write('Trying to copy this file. With luck there will be two!')
copytest.close()

copytest = open('d:\\code\\python-practice\\built-in-python-practice\\copytest.txt')
copytext = copytest.read()
print(copytext)


def makeacopy(file1):
    original = open(file1)
    print(dir(original))
    dupetext = original.read()
    print(dupetext)
    original.close()
    dupe = open('d:\\code\\python-practice\\built-in-python-practice\\dupe.txt', 'w')
    dupe.write(str(dupetext))
    dupe.close()

makeacopy('d:\\code\\python-practice\\built-in-python-practice\\copytest.txt')