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
        self.assertTrue("John Doe" in response.data.decode())

    def test_get_all_employees(self):
        response = self.app.get('/employees')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_add_employees(self):
        data = {
        "idemployees": "31",
        "last_name": "Abian",
        "first_name": "Vincent",
        "age": "22",
        "department": "Finance",
        "skills_idskills": "8"
    }
        response = self.app.post('/employees', json=data)
        print(response.status_code, response.get_data(as_text=True))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["message"], "employee added successfully")

    def test_update_employees(self):
        data = {
        "idemployees": "31",
        "last_name": "Abian",
        "first_name": "Update",
        "age": "22",
        "department": "IT",
        "skills_idskills": "3"
    }
        response = self.app.put('/employees/31', json=data)
        print(response.status_code, response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "employee updated successfully")

    

if __name__ == '__main__':
    unittest.main()