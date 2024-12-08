import unittest
import json
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_check_specific_employee_exists(self):
        response = self.app.get('/employees')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(any(emp['Full_Name'] == "John Doe" for emp in data))
   
if __name__ == '__main__':
    unittest.main()