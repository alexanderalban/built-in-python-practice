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

