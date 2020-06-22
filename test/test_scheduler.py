import unittest
from unittest import TestCase
from routes.scheduler import build_unique_expense, build_unique_income, add_monthly_expenses, add_monthly_incomes
from src.routes.router import app
from src.services.config import db
from flask import json


class SchedulerTest(TestCase):

    def setUp(self):
        db.expenses.drop()
        db.incomes.drop()
        self.client = app.test_client()

    def test_build_unique_expense(self):
        expense = {"_id": "id", "category": "transporte", "amount": 200, "description": "Sube", "account": "debito",
                   "date": "date", "user_email": "mauro@mauro.com", "etype": "mensual"}
        unique_expense = build_unique_expense(expense)
        self.assertEqual(unique_expense["etype"], "unico")
        self.assertRaises(KeyError, lambda: unique_expense["_id"])

    def test_build_unique_income(self):
        income = {"_id": "id", "category": "venta", "amount": 8200, "description": "Amplificador", "account": "debito",
                  "date": "date", "user_email": "mauro@mauro.com", "itype": "mensual"}
        unique_income = build_unique_income(income)
        self.assertEqual(unique_income["itype"], "unico")
        self.assertRaises(KeyError, lambda: unique_income["_id"])

    def test_add_monthly_expenses(self):
        monthly_expense = {"body": {"category": "transporte", "amount": 200, "description": "Sube", "account": "debito",
                   "date": "2020-06-11T21:54:35.041Z", "user_email": "test@user.com", "type": "mensual"}}
        self.client.post('/expense/add/', json=monthly_expense)

        filter = {"body": {"user_email": "test@user.com", "filter": {"type": "unico"}}}

        expenses_before_scheduler = self.client.post('/expense/filter/', json=filter)
        response_list = json.loads(expenses_before_scheduler.data)
        self.assertEqual(0, len(response_list))

        add_monthly_expenses()

        expenses_after_scheduler = self.client.post('/expense/filter/', json=filter)
        response_list_2 = json.loads(expenses_after_scheduler.data)
        self.assertEqual(1, len(response_list_2))

    def test_add_monthly_incomes(self):
        monthly_income = {"body": {
                                "category": "venta", "amount": 8200, "description": "Amplificador", "account": "debito",
                                "date": "2020-04-10T21:56:30.518Z", "user_email": "test@user.com", "type": "mensual"}
}
        self.client.post('/income/add/', json=monthly_income)

        filter = {"body": {"user_email": "test@user.com", "filter": {"type": "unico"}}}

        incomes_before_scheduler = self.client.post('/income/filter/', json=filter)
        response_list = json.loads(incomes_before_scheduler.data)
        self.assertEqual(0, len(response_list))

        add_monthly_incomes()

        incomes_after_scheduler = self.client.post('/income/filter/', json=filter)
        response_list_2 = json.loads(incomes_after_scheduler.data)
        self.assertEqual(1, len(response_list_2))


if __name__ == '__main__':
    unittest.main()