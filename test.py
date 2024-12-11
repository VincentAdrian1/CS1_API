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
        "department": "IT",
        "skills_idskills": "11"
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
        "department": "Finance",
        "skills_idskills": "8"
    }
        response = self.app.put('/employees/31', json=data)
        print(response.status_code, response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "employee updated successfully")

    def test_delete_employee(self):
        response = self.app.delete('/employees/24')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "employee deleted successfully")
        self.assertIn("rows_affected", data)
        self.assertEqual(data["rows_affected"], 1)  
    
    def test_delete_employee_nonexistent_id(self):
        response = self.app.delete('/employee/32')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 404)
        self.assertIn("Error", data)
        self.assertIn("employee not found", data["Error"])

    def test_get_all_skills(self):
        response = self.app.get('/skills')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_get_skills_by_department(self):
        response = self.app.get('/skills_dept', query_string={'department': 'IT'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue('IT' in data['department'])
        self.assertGreater(len(data['skills']), 0)

    def test_add_skills(self):
        data = {
            "idskills": "11",
            "skill_name": "Python"
        }
        response = self.app.post('/skills', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["message"], "skill added successfully")

    def test_update_skills(self):
        data = {
            "idskills":"11",
            "skill_name": "Advanced Python"
        }
        response = self.app.put('/skills/11', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "skill updated successfully")

    def test_delete_skills(self):
        response = self.app.delete('/skills/11')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "skill deleted successfully")
    
if __name__ == '__main__':
    unittest.main()