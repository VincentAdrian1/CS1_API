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

    def test_get_employee_by_id(self):
        response = self.app.get('/employees/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertEqual(data[0]['idemployees'], 1)

    def test_get_all_employees(self):
        response = self.app.get('/employees')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
   
if __name__ == '__main__':
    unittest.main()