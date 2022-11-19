from flask import Flask

import IPN_Scrapper
from IPN_Scrapper import get_question_list

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello test'

@app.route('/api')
def hello_world2():
    return 'hello test2'


@app.route("/api/<string:fraza>")
def get_questions(fraza):
    pytania = IPN_Scrapper.get_question_list(fraza)
    print(pytania)
    return pytania


if __name__ == '__main__':
    app.run()