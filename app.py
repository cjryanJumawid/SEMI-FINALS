import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1> Full name : Cj Ryan Jumawid  '
            'Year and Section : 3rd year BSIT A 2nd Lab  '
            'Subject :  ITE 322  System Integration and Architecture 1 '
            'Semi-finals exam </h1>')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
