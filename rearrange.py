import sys
import random 


arguments = sys.argv[1:]

def rearrange():
    for random_arg in arguments:
        random_arg = random.randint(0, len(arguments)-1)
        print(arguments[random_arg])
    
rearrange()


# filename = "/Users/Funkhauser/dev/Courses/CS-1.2/words.txt"

# my_file = open(filename, "r")

# lines = my_file.readlines()

# random_index = randiint(0, len(lines)-1)
# lines[1]

# print(lines)



# def read_words_from_input(input):
#     with open() as f:
#         content = f.read()
#         content = content.split()
#         return content

# def words_printed_random(input):
#     content = read_words_from_file(poem_file)
#     random.shuffle(content)
#     for i in content:
#         print (i)
