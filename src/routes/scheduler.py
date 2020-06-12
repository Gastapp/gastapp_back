from datetime import date
import datetime

import copy
from apscheduler.schedulers.background import BackgroundScheduler
from dateutil import parser
from controllers import expensesController, incomesController
from model.types import Type

scheduler = BackgroundScheduler()


def build_unique_expense(expense):
    del expense['_id']
    expense["etype"] = Type.unico.value
    expense["date"] = parser.isoparse(datetime.datetime.now().isoformat())
    return expense


def build_unique_income(income):
    del income['_id']
    income["itype"] = Type.unico.value
    income["date"] = parser.isoparse(datetime.datetime.now().isoformat())
    return income


def add_monthly_expenses():
    print("gastos")
    new_incomes = list(expensesController.find_all_monthly_expenses())

    if new_incomes:
        new_incomes = map(build_unique_income, new_incomes)
        expensesController.save_all(new_incomes)


def add_monthly_incomes():
    print("ingresos")
    new_incomes = list(incomesController.find_all_monthly_incomes())

    if new_incomes:
        new_incomes = map(build_unique_expense, new_incomes)
        incomesController.save_all(new_incomes)


def start_scheduler():
    #scheduler.add_job(add_monthly_expenses, 'interval', seconds=10)
    #scheduler.add_job(add_monthly_incomes, 'interval', seconds=10)
    scheduler.add_job(add_monthly_expenses, 'cron', day='1')
    scheduler.add_job(add_monthly_incomes, 'cron', day='1')
    scheduler.start()
