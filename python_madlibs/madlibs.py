"""
    madlibs.py - Generate MadLibs
"""

import random
from flask import Flask, jsonify, render_template

app = Flask(__name__)

nouns = ['half', 'goal', 'house', 'memory', 'doll', 'bottom', 'meal',
         'question', 'memory card', 'screw', 'basis', 'stamp', 'sanctuary']
foods_1 = ['cake', 'chicken', 'meat', 'French dip', 'apples', 'avacado']
foods_2 = ['sushi', 'broccoli', 'beer', 'salad', 'artichoke', 'bacon']
verbs = ['remember', 'alert', 'exclaim', 'squish', 'darken', 'verify',
         'reconsider', 'massage', 'pressure', 'shamble', 'babysit', 'tisk']
adverbs = ['influentially', 'unenlightenedly', 'garrulously', 'unreasonably',
           'lovingly', 'selflessly', 'garrulously', 'coordinately', 'clearly']
adjectives = ['secret', 'savoy', 'free', 'apathetic', 'parliamentary',
              'knotty', 'absorbed', 'overconfident', 'firm', 'humdrum']


@app.route('/', methods=['GET'])
def generate():
    """
    Generate texts.
    """
    response = {
        'header': 'The Beatles - Lucy In The Sky With Diamonds',
        'noun': nouns[random.randint(0, len(nouns) - 1)],
        'food_1': foods_1[random.randint(0, len(foods_1) - 1)],
        'food_2': foods_2[random.randint(0, len(foods_2) - 1)],
        'verb': verbs[random.randint(0, len(verbs) - 1)],
        'adverb': adverbs[random.randint(0, len(adverbs) - 1)],
        'adjective': adjectives[random.randint(0, len(adjectives) - 1)],
    }
    return render_template('landing.html', data=response)



if __name__ == '__main__':
    app.run()
