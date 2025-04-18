from flask import Flask, request, jsonify
from decrypt import decrypt
from datetime import datetime
from get_day import get_day_of_week_name
from collections import defaultdict

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route('/hello-world/<name>')
def hello(name):
    weekday = datetime.today().weekday()
    day_of_week_name = get_day_of_week_name(weekday)
    return f"Привет, {name}. {day_of_week_name}!"


@app.route('/decrypt', methods=['POST'])
def decrypt_message():
    data = request.data.decode('utf-8')
    result = decrypt(data)
    return result


storage = defaultdict(lambda: defaultdict(int))


@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    try:
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])
        if month < 1 or month > 12 or day < 1 or day > 31:
            raise ValueError("Неверно написана дата")
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    storage.setdefault(year, {}).setdefault(month, 0)
    storage[year][month] += number

    return "Расход успешно добавлен"


@app.route('/calculate/<int:year>')
def calculate_year(year):
    if year not in storage:
        return jsonify({"error": "Нет данных для выбранного года"}), 404

    total_expense = sum(storage[year].values())
    return jsonify({"year": year, "total_expense": total_expense})


@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    if year not in storage or month not in storage[year]:
        return jsonify({"error": "Нет данных для выбранного месяца и года"}), 404

    total_expense = storage[year][month]
    return jsonify({"year": year, "month": month, "total_expense": total_expense})


if __name__ == '__main__':
    app.run(debug=True)
