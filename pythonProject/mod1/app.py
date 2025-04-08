import datetime
import os
import random
import re
from datetime import datetime
from random import choice

from flask import Flask

app = Flask(__name__)


def update_time():
    global now
    now = datetime.now().utcnow()


@app.route('/test')
def test_function():
    update_time()
    return f'Это тестовая страничка, ответ сгенерирован в {now}'


@app.route('/hello_world')
def hello_world():
    return f'Привет, мир!'


cars = ["Chevrolet", "Renault", "Ford"]


@app.route('/cars')
def get_cars():
    return ', '.join(cars)


cats = ["корниш-рекс", " русская голубая", " шотландская вислоухая", " мейн-кун", " манчкин"]


@app.route('/cats')
def get_cats():
    return choice(cats)


@app.route('/get_time/now')
def get_time():
    update_time()
    return f'Сейчас {now}'


#
# @app.route('/get_time/future')
# def get_time_future():
#     update_time()
#     time_after_hour = now + datetime.timedelta(hours=1)
#     return f'Текущее время +1 час {time_after_hour}'
#

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

words_list = []


def load_words():
    global words_list
    with open(BOOK_FILE, 'r', encoding='utf-8') as book:
        text = book.read()
        words_list = re.findall(r'\b\w+\b', text)


def get_random_word():
    if not words_list:
        load_words()
    return random.choice(words_list)


@app.route('/get_random_word')
def get_random_word():
    word = get_random_word()
    return f'Случайное слово: {word}'




@app.route('/counter')
def get_counter():
    get_counter.visits += 1  # Увеличиваем счетчик на 1
    return f'Страница была открыта {get_counter.visits} раз(а).'

get_counter.visits = 0

if __name__ == '__main__':
    app.run(debug=True)
