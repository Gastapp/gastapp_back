import unittest
from unittest import TestCase
from src.routes.router import app
from src.services.config import db


class LoginRegisterTest(TestCase):

    def setUp(self):
        db.users.drop()
        self.client = app.test_client()

    def test_login_exception(self):
        fake_user = {"email": "fake email", "password": "12345"}
        response = self.client.post('/login/', json=fake_user)
        self.assertEqual(response.status, "401 UNAUTHORIZED")

    def test_register_and_login_successfully(self):
        new_user = {"name": "new user", "email": "email@test.com", "password": "12345"}
        response_register = self.client.post('/register/', json=new_user)
        response_login = self.client.post('/login/', json={"email": "email@test.com", "password": "12345"})
        self.assertEqual(response_register.status, "200 OK")
        self.assertEqual(response_login.status, "200 OK")


if __name__ == '__main__':
    unittest.main()