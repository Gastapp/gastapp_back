from flask import Flask, request, json
from werkzeug.exceptions import HTTPException

from controllers import userController
from exceptions.LoginException import LoginException
from src.controllers import expensesController, categoriesController
from bson.json_util import dumps

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hola mundo"


@app.route('/expense/get_all/', methods=['GET'])
def get_expenses():
    id_user = request.args.get('id_user')
    result = expensesController.get_all_user_expenses(id_user)
    return dumps(result)


@app.route('/expense/get_lastest/', methods=['GET'])
def get_lastest_expenses():
    id_user = request.args.get('id_user')
    result = expensesController.get_lastest_user_expenses(id_user)
    return dumps(result)


@app.route('/expense/get_by/category/', methods=['GET'])
def get_by_category():
    id_user = request.args.get('id_user')
    category = request.args.get('category')
    result = expensesController.get_all_by_category(id_user, category)
    return dumps(result)


@app.route('/expense/get_total_by/user/', methods=['GET'])
def get_total_by_user():
    id_user = request.args.get('id_user')
    result = expensesController.get_total_expenses_amount_by_user(id_user)
    return dumps(result)


@app.route('/expense/get_total_by/category/', methods=['GET'])
def get_total_by_category():
    id_user = request.args.get('id_user')
    category = request.args.get('category')
    result = expensesController.get_total_expenses_amount_by_category(id_user, category)
    return dumps(result)


@app.route('/category/get_all/', methods=['GET'])
def get_all_categories():
    return dumps(categoriesController.get_all())


@app.route("/expense/add/", methods=['POST'])
def add_expense():
    data = request.get_json()
    expensesController.add_expense(data["body"])
    return "200"


@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    return userController.login(data)


@app.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    return userController.register(data)


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
