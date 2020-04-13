from flask import Flask, request
from exceptions import ImputNotJsonException
from src.controllers import expensesController

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola mundo"


@app.route('/gastos', methods=['GET'])
def get_expenses():
    return expensesController.get_all()


@app.route('/gastos', methods=['POST'])
def save_expense():
    if not request.is_json:
        raise ImputNotJsonException
    expensesController.save(request.get_json)
    return 200
