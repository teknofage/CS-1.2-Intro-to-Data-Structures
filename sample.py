from random import randint

def weighted_sample(histogram):
    """return a word from this histogram, randomly sampled by weighting each word's probability of being chosen by its observed frequency."""
    tokens = sum([count for word, count in histogram.items()]) # Count total tokens
    dart = randint(1, tokens) # throw a dart at the number line
    fence = 0 # border of where each word splits the number line
    for word, count in histogram.items(): # loop over each word and its count
        fence += count # Move this word's fence broder to the right
        if fence >= dart: # Check if this word's fence is past the dart
            return word # Fence is past the dart, so choose this word