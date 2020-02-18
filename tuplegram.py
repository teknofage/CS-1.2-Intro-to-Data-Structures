import sys as sys
from dictogram import get_index

# filename = "blog_post.txt"
# filename = "morte_d'arthur(bk1-2).txt"
filename = "words.txt"

def tuplegram(lines):
    """list of lists"""
    tuple_list = []
    lines = open(filename, "r")
    
    for word in lines:
        word = word.rstrip()
        index = get_index(word, tuple_list)
        
        if index == -1: 
            # first instance
            tuple_list.append((word,1))
        else:
            tuple_list[index] = (word, tuple_list[index][1]+1)
    print(tuple_list)
    return tuple_list

def unique_words(histogram):
    """takes a histogram argument and returns the total count of unique words in the histogram"""
    total_count = 0
    for k,v in word_histogram.items():
        if v == 1:
            total_count +=1
            
    print(total_count)
            
            
def frequency(word, histogram):
    """takes a word and histogram argument and returns the number of times that word appears in a text."""
    frequencies = []
    return histogram[word]

def get_lines(filename):
    with open(filename, "r") as my_file:
        lines = my_file.readlines
    return lines

if __name__ == "__main__":
    wordList = get_lines(sys.argv[1])
    tuplistic = tuplegram(get_lines(sys.argv[1]))
    print(unique_words(tuplistic))
    '''print("Unique words:" + str(unique_words(tuplistic)))
    print("# of 'and':" + str(frequency(tulplistic, "and")))
    print("# of 'they':" +str(frequency(tuplistic, "they")))'''
    