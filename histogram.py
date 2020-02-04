filename = "blog_post.txt"
# filename = "words.txt"
lines = open(filename, "r")



def histogram(lines):
    """takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text."""
    word_histogram = {}
    for word in lines:
        word = word.rstrip()
        if word not in word_histogram.keys():
            word_histogram[word]=1
        else:
            word_count_value = word_histogram.get(word)
            word_count_value += 1
            word_histogram[word] = word_count_value
    
    print (word_histogram)
histogram(lines)
    
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
        
def get_index(word, listogram):
    current_index = 0
    for item in listogram:
        if item[0] == word:
            return current_index
        else:
            current_index += 1
    return -1
    
def listogram(lines):
    listogram = []
    for word in lines:
        word = word.rstrip()
        index = get_index(word, listogram)
        if index == -1:
            listogram.append([word,1])
        else:
            listogram[index][1] += 1
    return listogram


# listogram = []
# for wor in words:
#     if word in listogram:
#     add 1 to count
# else: 
#   make a new entry for value 1
#     listogram.append([word,1])