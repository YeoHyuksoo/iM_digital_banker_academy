import os
import string

print(os.name)
print(os.getcwd())
# print(os.path.join(os.getcwd(), "test"))
# print(os.getcwd())
# os.mkdir(os.path.join(os.getcwd(), "test"))

import math

print(math.pi)
print(math.sin(math.pi))

import random

print("\n=========RANDOM===========")
print(random.random())
print(random.uniform(5,10))
print(random.randint(1,100))
print(random.randrange(0, 100, 2))
print(random.choice('abcdefg'))
print(random.sample(string.ascii_uppercase, 10))

nums = [n for n in range(10)]
random.shuffle(nums)
print(nums)