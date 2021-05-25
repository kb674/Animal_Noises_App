from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_animal(self):
        for _ in range(20):
            response = self.client.get(url_for('get_animal'))
            self.assertIn(response.data.decode("utf-8"),["cow", "dog", "fox"])
        
    def test_get_noise(self):
            response = self.client.post(url_for('get_noise'), data="cow")
            self.assertEqual(response.data.decode("utf-8"),"moo")
    