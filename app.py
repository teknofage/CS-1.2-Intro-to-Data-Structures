from flask import Flask
from histogram import histogram
from sample import weighted_sample


app = Flask(__name__)


@app.route('/')
def generate_words():
    # build a histogram
    my_file = open("./words.txt", "r")
    lines = my_file.readlines()
    my_histogram = histogram(lines)
    print(my_histogram)
    
    sentence = ""
    num_words = 10
    for i in range (num_words):
        word = weighted_sample(my_histogram)
        sentence += " " + word
    return sentence

if __name__ == '__ main__':
    app.run()