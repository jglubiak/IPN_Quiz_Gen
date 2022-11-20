from flask import Flask

import IPN_Scrapper
from IPN_Scrapper import create_quiz

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello test'

@app.route('/api')
def hello_world2():
    return 'hello test2'


@app.route("/api/<string:fraza>")
def get_questions(fraza):
    quiz = create_quiz(fraza)
    return quiz
    # pytania = IPN_Scrapper.get_question_list(fraza)
    # print(pytania)
    # return pytania


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)
