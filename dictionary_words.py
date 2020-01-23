import sys as sys
from random import randint
import random

arguments = int(sys.argv[1])

filename = "/usr/share/dict/words"

my_file = open(filename, "r")
lines = my_file.readlines()

def rearrange():
    for random_arg in range(arguments):
        random_words = random.randint(1, len(lines) -1)
        print(lines[random_words])
    
rearrange()

