from flask import Flask, request
from exceptions import ImputNotJsonException
from src.controllers import expensesController
from bson.json_util import dumps

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola mundo"


@app.route('/expense/get_all', methods=['GET'])
def get_expenses():
    result = expensesController.get_all()
    return dumps(result)

@app.route('/expense/get_by/category', methods=['POST'])
def get_by_category():
    category = request.get_json()['category']
    result = expensesController.get_by_category(category)
    return result


@app.route('/expense/add', methods=['POST'])
def save_expense():
    expensesController.save(request.get_json())
    return "200"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
