from flask import Flask, request
from exceptions import ImputNotJsonException
from src.controllers import expensesController

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola mundo"


@app.route('/gastos', methods=['GET'])
def get_expenses():
    result = expensesController.get_all()
    return str(list(result))


@app.route('/gastoss', methods=['POST'])
def save_expense():
    print("DALEEEEE")
    print("Data: ", format(request.get_json(force=True)))
    expensesController.save(request.get_json(force=True))
    return "200"


if __name__ == "__main__":
    app.run()
