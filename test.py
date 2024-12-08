import unittest
import json
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()