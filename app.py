from flask import Flask
from dictogram import histogram
from sample import weighted_sample
from markov import MarkovChain


app = Flask(__name__)


@app.route('/')
def generate_words():
#     # build a histogram
    '''my_file = open("./fish.txt", "r")
    lines = my_file.readlines()
    words_list = []
    for line in lines:
        words = line.split()
        for word in words:
            words_list.append(word.rstrip())'''
#     my_histogram = histogram(lines)
#     print(my_histogram)
    
#     sentence = ""
#     num_words = 10
#     for i in range (num_words):
#         word = weighted_sample(my_histogram)
#         sentence += " " + word
#     return sentence

    markovchain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
    return markovchain.walk(10)

if __name__ == '__ main__':
    app.run()