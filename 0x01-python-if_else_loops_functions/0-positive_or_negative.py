#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive\n".format(number))
else if number == 0:
    print(f"{number} is zero\n")
else:
    print("{} is negative\n".format(number))
