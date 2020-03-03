from flask import Flask
from dictogram import histogram
from sample import weighted_sample
from markov import MarkovChain


app = Flask(__name__)


@app.route('/')
def generate_words():
    '''my_histogram = (lines)
    
    sentence = ""
    num_words = 10
    for i in range (num_words):
        word = weighted_sample(my_histogram)
        sentence += " " + word
    return sentence'''

    markovchain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
    return markovchain.walk(10)

if __name__ == '__ main__':
    app.run()