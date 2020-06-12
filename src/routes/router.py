from flask import Flask, request, json
from werkzeug.exceptions import HTTPException

from routes.scheduler import start_scheduler
from src.controllers import expensesController, categoriesController, userController, incomesController, accountsController, typesController
from bson.json_util import dumps

app = Flask(__name__)


@app.route("/")
def hello():
    return "Funciona", 200


#           EXPENSES         #


@app.route("/expense/add/", methods=['POST'])
def add_expense():
    data = request.get_json()
    expensesController.add_expense(data["body"])
    return "200"


@app.route('/expense/edit_expense/', methods=['POST'])
def edit_expense():
    data = request.get_json()
    expensesController.edit_expense(data["body"])
    return "200"


@app.route('/expense/delete/', methods=['POST'])
def delete_expense():
    data = request.get_json()
    expensesController.delete_expense(data["body"])
    return "200"


@app.route('/expense/get_all/', methods=['GET'])
def get_expenses():
    user_email = request.args.get('user_email')
    result = expensesController.get_all_user_expenses(user_email)
    return dumps(result)


@app.route('/expense/get_latest/', methods=['GET'])
def get_latest_expenses():
    user_email = request.args.get('user_email')
    result = expensesController.get_lastest_user_expenses(user_email)
    return dumps(result)


@app.route('/expense/filter/', methods=['POST'])
def filter_expenses():
    data = request.get_json()
    user_email = data["body"]["user_email"]
    filter_data = data["body"]["filter"]
    result = expensesController.filter_expenses(user_email, filter_data)
    return dumps(result), 200, {'Content-Type': 'application/json'}


@app.route('/expense/get_total_by/user/', methods=['GET'])
def get_total_expenses_by_user():
    user_email = request.args.get('user_email')
    result = expensesController.get_total_expenses_amount_by_user(user_email)
    return dumps({"total": result}), 200, {'Content-Type': 'application/json'}


@app.route('/expense/get_types/', methods=['GET'])
def get_expense_types():
    return dumps(typesController.get_all())


#           INCOMES         #


@app.route("/income/add/", methods=['POST'])
def add_income():
    data = request.get_json()
    incomesController.add_income(data["body"])
    return "200"


@app.route('/income/edit_expense/', methods=['POST'])
def edit_income():
    data = request.get_json()
    incomesController.edit_income(data["body"])
    return "200"


@app.route('/income/delete/', methods=['POST'])
def delete_income():
    data = request.get_json()
    incomesController.delete_income(data["body"])
    return "200"


@app.route('/income/get_all/', methods=['GET'])
def get_incomes():
    user_email = request.args.get('user_email')
    result = incomesController.get_all_user_incomes(user_email)
    return dumps(result)


@app.route('/income/get_latest/', methods=['GET'])
def get_latest_incomes():
    user_email = request.args.get('user_email')
    result = incomesController.get_lastest_user_incomes(user_email)
    return dumps(result)


@app.route('/income/filter/', methods=['POST'])
def filter_incomes():
    data = request.get_json()
    user_email = data["body"]["user_email"]
    filter_data = data["body"]["filter"]
    result = incomesController.filter_incomes(user_email, filter_data)
    return dumps(result), 200, {'Content-Type': 'application/json'}


@app.route('/income/get_total_by/user/', methods=['GET'])
def get_total_incomes_by_user():
    user_email = request.args.get('user_email')
    result = incomesController.get_total_incomes_amount_by_user(user_email)
    return dumps({"total": result}), 200, {'Content-Type': 'application/json'}


@app.route('/income/get_types/', methods=['GET'])
def get_income_types():
    return dumps(typesController.get_all())


#           CATEGORY         #


@app.route('/category/expense/get_all/', methods=['GET'])
def get_all_expense_categories():
    return dumps(categoriesController.get_all_for_expenses())


@app.route('/category/income/get_all/', methods=['GET'])
def get_all_income_categories():
    return dumps(categoriesController.get_all_for_incomes())

#           ACCOUNT         #


@app.route('/account/expense/get_all/', methods=['GET'])
def get_all_expense_accounts():
    return dumps(accountsController.get_all_for_expenses())


@app.route('/account/income/get_all/', methods=['GET'])
def get_all_income_accounts():
    return dumps(accountsController.get_all_for_incomes())


#           USER         #


@app.route("/login/", methods=['POST'])
def login():
    data = request.get_json()
    return userController.login(data), 200, {'Content-Type': 'application/json'}


@app.route("/register/", methods=['POST'])
def register():
    data = request.get_json()
    return userController.register(data), 200, {'Content-Type': 'application/json'}


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
    start_scheduler()
    app.run(use_reloader=False, debug=True, host='0.0.0.0')
