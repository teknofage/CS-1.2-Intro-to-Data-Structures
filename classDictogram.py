from __future__ import division, print_function
import random

class Dictogram(dict):

    def __init__(self, word_list=None):
        '''Initializes the dictogram properties'''
        super(Dictogram, self).__init__()
        self.word_list = word_list
        self.histogram = {}
        # self.dictionary_histogram = self.build_dictogram()

        self.tokens = 0
        self.types = 0
        
        if word_list is not None:
            for word in word_list:
                self.add_count(word)
                
    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        
        self.tokens += count
        if word in self.keys():
            self[word] += count
        else:
            self[word] = count 
            self.types += 1

    def build_dictogram(self, lines): 
        '''Creates a histogram dictionary using the word_list property and returns it'''

        filename = "words.txt"
        word_frequency = {}
        self.word_histogram = {}
        self.lines = open(filename, "r")
        
        for word in lines:
            word = word.rstrip()
            if word not in self.word_histogram.keys():
                self.word_histogram[word]=1
            else:
                word_count_value = self.word_histogram.get(word)
                word_count_value += 1
                self.word_histogram[word] = word_count_value
    
        return self.word_histogram

    def frequency(self, word):
        '''returns the frequency or count of the given word in the dictionary histogram, or 0 if the word is not found'''
        frequencies = []
        # if word in self.word_histogram:
        #     return self.histogram[word]
        # else:
        #     return 0
        
        for key, value in self.items():
            if word == key:
                return value
        return 0

    def unique_words(self):
        '''returns the number of unique words in the dictionary histogram'''
        #TODO: use your unique words function as a starting point to complete this method
        """takes a histogram argument and returns the total count of unique words in the histogram"""
        total_count = 0
        for k,v in self.word_histogram.items():
            if v == 1:
                total_count +=1
            
        print(total_count)

    def sample(self):
        '''Randomly samples from the dictionary histogram based on the frequency, returns a word'''
        random_num = random.randint(0, self.tokens-1)  # gets random number
        weight=0
        for key, value in self.items():
            weight += value
            if weight > random_num:
                return key

def print_dictogram(word_list):
    '''Creates a dictionary based histogram (dictogram) and then prints out its properties and samples from it'''

    print()
    print('Dictionary Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    dictogram = Dictogram(word_list)
    print('dictogram: {}'.format(dictogram))
    print('{} tokens, {} types'.format(dictogram.tokens, dictogram.types))
    for word in word_list[-2:]:
        freq = dictogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_dictogram_samples(dictogram)

def print_dictogram_samples(dictogram):
    '''Compares sampled frequency to observed frequency'''

    print('Dictionary Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [dictogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
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
    for word, count in dictogram.items():
        # Calculate word's observed frequency
        observed_freq = count / dictogram.tokens
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

print_dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])