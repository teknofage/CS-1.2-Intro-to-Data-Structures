from __future__ import division, print_function
from random import randint
import random

class Listogram(list):

    def __init__(self, word_list=None):
        '''Initializes the listogram properties'''
        super(Listogram, self).__init__()

        # self.list_histogram = add
        self.tokens = 0
        self.types = 0

        if word_list is not None:
            for word in word_list:
                self.add_count(word)
                
    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        
        index = self.get_index(word)
        if index is not None:
            old_count = self[index][1]
            self[index] = [word, old_count + count]
            self.tokens += count
        else:
            self.append((word, count)) 
            self.tokens += count
            self.types += 1

    def get_index(self, word):
        '''searches in the list histogram parameter and returns the index of the inner list that contains the word if present'''
        
        for index, item in enumerate(self):
            if item[0] == word:
                return index
        return None

    def frequency(self, word):
        '''returns the frequency or count of the given word in the list of lists histogram'''
        frequencies = []
        for index in range(len(self)):
            if self[index][0] == word:
                return self[index][1]
        return 0
        
    def unique_words(self):
        '''returns the number of unique words in the list of lists histogram'''
        """takes a histogram argument and returns the total count of unique words in the histogram"""
        total_count = 0
        for inner_list in self.list_histogram:
            total_count +=1
            
        print(total_count)


    def sample(self):
        '''Randomly samples from the list of list histogram based on the frequency, returns a word'''

        """return a word from this histogram, randomly sampled by weighting each word's probability of being chosen by its observed frequency."""
            
        random_num = random.randint(0, self.tokens-1)  # gets random number
        weight=0
        for index, item in enumerate(self):
            # print(f"occur: {item}")
            weight += item[1]
            
            if weight > random_num:
                return item[0]

def print_listogram(word_list):
    '''Creates a list based histogram (listogram) and then prints out its properties and samples from it'''

    print()
    print('List of Lists Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    listogram = Listogram(word_list)
    print('listogram: {}'.format(listogram))
    print('{} tokens, {} types'.format(listogram.tokens, listogram.types))
    for word in word_list[-2:]:
        freq = listogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_listogram_samples(listogram)

def print_listogram_samples(listogram):
    '''Compares sampled frequency to observed frequency'''

    print('List of Lists Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [listogram.sample() for _ in range(10000)]
    samples_hist = Listogram(samples_list)
    print('samples: {}'.format(samples_hist))
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
    for item in listogram:
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
