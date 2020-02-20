from random import randint

class Listogram:

    def __init__(self, word_list):
        '''Initializes the listogram properties'''

        self.word_list = word_list
       
        self.list_histogram = self.build_listogram()

        self.tokens = self.get_num_tokens()
        self.types = self.unique_words()

    def build_listogram(self): 
        '''Creates a histogram list of lists using the word_list property and returns it'''

        #TODO: use your listogram function as a starting point to complete this method
        filename = "words.txt"
        listogram = []
        self.lines = open(filename, "r")
        for word in self.lines:
            word = word.rstrip()
            index = self.get_index(word, listogram)
            if index == -1: 
                # first instance
                listogram.append([word,1])
            else:
                listogram[index][1] += 1
                # update count
        return listogram

    def get_num_tokens(self):
        '''gets the number of tokens in the listogram'''

        tokens = 0
        for item in self.list_histogram:
            tokens += item[1]
        return tokens

    def get_index(self, word, list_histogram):
        '''searches in the list histogram parameter and returns the index of the inner list that contains the word if present'''
        #TODO: use your get_index function as a starting point to complete this method
        current_index = 0
        for item in list_histogram:
            if item[0] == word:
                return current_index
            else:
                current_index += 1
        return -1

    def frequency(self, word):
        '''returns the frequency or count of the given word in the list of lists histogram'''
        #TODO: use your frequency and get_index function as a starting point to complete this method
        #You will need to adapt it a little bit to work with listogram
        frequencies = []
        return self.list_histogram[word]
        
    def unique_words(self):
        '''returns the number of unique words in the list of lists histogram'''
        #TODO: use your unique words function as a starting point to complete this method
        #You will need to adapt it a little bit to work with listogram
        """takes a histogram argument and returns the total count of unique words in the histogram"""
        total_count = 0
        for inner_list in self.list_histogram:
            total_count +=1
            
        print(total_count)


    def sample(self):
        '''Randomly samples from the list of list histogram based on the frequency, returns a word'''

        #TODO: use your sample function as a starting point to complete this method 
        #You will need to adapt it a little bit to work with listogram
        """return a word from this histogram, randomly sampled by weighting each word's probability of being chosen by its observed frequency."""
        tokens = sum([count for word, count in histogram.items()]) # Count total tokens
        dart = randint(1, tokens) # throw a dart at the number line
        fence = 0 # border of where each word splits the number line
        for word, count in histogram.items(): # loop over each word and its count
            fence += count # Move this word's fence broder to the right
            if fence >= dart: # Check if this word's fence is past the dart
                return word # Fence is past the dart, so choose this word

def print_listogram(word_list):
    '''Creates a list based histogram (listogram) and then prints out its properties and samples from it'''

    print()
    print('List of Lists Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    listogram = Listogram(word_list)
    print('listogram: {}'.format(listogram.list_histogram))
    print('{} tokens, {} types'.format(listogram.tokens, listogram.types))
    for word in word_list[-2:]:
        freq = listogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_dictogram_samples(listogram)

def print_dictogram_samples(listogram):
    '''Compares sampled frequency to observed frequency'''

    print('List of Lists Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [listogram.sample() for _ in range(10000)]
    samples_hist = Listogram(samples_list)
    print('samples: {}'.format(samples_hist.list_histogram))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for item in listogram.list_histogram:
        word = item[0]
        count = item[1]
        # Calculate word's observed frequency
        observed_freq = count / listogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()

print_listogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])