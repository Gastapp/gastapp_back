from flask import Flask, request
from exceptions import ImputNotJsonException
from src.controllers import expensesController

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola mundo"


@app.route('/expense/get_all', methods=['GET'])
def get_expenses():
    result = expensesController.get_all()
    return str(list(result))


@app.route('/expense/add', methods=['POST'])
def save_expense():
    expensesController.save(request.get_json())
    return "200"


if __name__ == "__main__":
    app.run()
