import unittest
from datetime import datetime
from unittest import TestCase
from src.builder import builder


class BuilderTest(TestCase):

    def test_build_user(self):
        mock_data = {"name": "username", "email": "fake@fake.com", "password": "12345"}
        user = builder.build_user(mock_data)
        self.assertEqual(user.name, mock_data["name"])
        self.assertEqual(user.email, mock_data["email"])
        self.assertIsNotNone(user.password)

    def test_build_expense_with_description(self):
        date = datetime.now()
        mock_data = {
            "user_email": "fake@fake.com",
            "amount": 100,
            "category": "ropa",
            "account": "efectivo",
            "date": date.isoformat(),
            "type": "unico",
            "description": "expense description"
        }

        expense = builder.build_expense(mock_data)
        self.assertEqual(expense.user_email, mock_data["user_email"])
        self.assertEqual(expense.amount, mock_data["amount"])
        self.assertEqual(expense.category, mock_data["category"])
        self.assertEqual(expense.account, mock_data["account"])
        self.assertEqual(expense.date.replace(microsecond=0), date.replace(microsecond=0))
        self.assertEqual(expense.etype, mock_data["type"])
        self.assertEqual(expense.description, mock_data["description"])

    def test_build_expense_without_description(self):
        date = datetime.now()
        mock_data = {
            "user_email": "fake@fake.com",
            "amount": 100,
            "category": "ropa",
            "account": "efectivo",
            "date": date.isoformat(),
            "type": "unico"
        }

        expense = builder.build_expense(mock_data)
        self.assertEqual(expense.user_email, mock_data["user_email"])
        self.assertEqual(expense.amount, mock_data["amount"])
        self.assertEqual(expense.category, mock_data["category"])
        self.assertEqual(expense.account, mock_data["account"])
        self.assertEqual(expense.date.replace(microsecond=0), date.replace(microsecond=0))
        self.assertEqual(expense.etype, mock_data["type"])
        self.assertEqual(expense.description, "")

    def test_build_income_with_description(self):
        date = datetime.now()
        mock_data = {
            "user_email": "fake@fake.com",
            "amount": 100,
            "category": "inversiones",
            "account": "efectivo",
            "date": date.isoformat(),
            "type": "mensual",
            "description": "income description"
        }

        income = builder.build_income(mock_data)
        self.assertEqual(income.user_email, mock_data["user_email"])
        self.assertEqual(income.amount, mock_data["amount"])
        self.assertEqual(income.category, mock_data["category"])
        self.assertEqual(income.account, mock_data["account"])
        self.assertEqual(income.date.replace(microsecond=0), date.replace(microsecond=0))
        self.assertEqual(income.itype, mock_data["type"])
        self.assertEqual(income.description, mock_data["description"])

    def test_build_income_without_description(self):
        date = datetime.now()
        mock_data = {
            "user_email": "fake@fake.com",
            "amount": 100,
            "category": "regalo",
            "account": "efectivo",
            "date": date.isoformat(),
            "type": "unico"
        }

        income = builder.build_income(mock_data)
        self.assertEqual(income.user_email, mock_data["user_email"])
        self.assertEqual(income.amount, mock_data["amount"])
        self.assertEqual(income.category, mock_data["category"])
        self.assertEqual(income.account, mock_data["account"])
        self.assertEqual(income.date.replace(microsecond=0), date.replace(microsecond=0))
        self.assertEqual(income.itype, mock_data["type"])
        self.assertEqual(income.description, "")


if __name__ == '__main__':
    unittest.main()
