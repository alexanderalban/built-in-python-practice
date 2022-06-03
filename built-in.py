# Practicing using the functions built into Python

# The abs function returns the absolute value of a number without it's sign (10 is 10, -10 is also 10). say you're counting how many steps a character
# was taking in a game. this would allow both forward and backward steps to be counted

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
print(int('123.456'))