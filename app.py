from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL
import logging

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "skill_gap"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


def data_fetch(query, params=None):
    try:
        cur = mysql.connection.cursor()
        cur.execute(query, params)
        data = cur.fetchall()
        cur.close()
        return data
    except Exception as e:
        logging.error(f"Error in data_fetch: {str(e)}")
        raise

def execute_query(query, params=None):
    try:
        cur = mysql.connection.cursor()
        cur.execute(query, params)
        mysql.connection.commit()
        rows_affected = cur.rowcount
        cur.close()
        return rows_affected
    except Exception as e:
        logging.error(f"Error executing query: {str(e)}")
        raise

def validate_input(info, required_fields):
    for field in required_fields:
        if field not in info:
            return False
    return True


@app.route('/employees')
def employees():
    try:
       query = """Select concat(employees.first_name, " ", employees.last_name) as Full_Name, 
                        idemployees, age, department, skills_idskills FROM employees"""
       data = data_fetch(query)
       return make_response(jsonify(data), 200)
    except Exception as e:
        return make_response(jsonify({"success": False, "error": str(e)}), 500)
    
@app.route("/employees/<int:id>")
def get_by_id(id):
    try:
        query = """Select concat(employees.first_name, " ", employees.last_name) as Full_Name, 
                        idemployees, age, department, skills_idskills FROM employees WHERE idemployees = %s"""
        data = data_fetch(query, (id,))
        return make_response(jsonify(data), 200)
    except Exception as e:
        return make_response(jsonify({"Error": "Internal server error"}), 500)

@app.route("/employees", methods=["POST"])
def add_employees():
    try:
        info = request.get_json()
        required_fields = ["idemployees", "last_name", "first_name", "age", "department", "skills_idskills"]
        
        if not validate_input(info, required_fields):
            return make_response(jsonify({"Error": "Missing required fields"}), 400)

        query = """INSERT INTO employees (idemployees, last_name, first_name, age, department, skills_idskills) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        params = (info["idemployees"], info["last_name"], info["first_name"], info["age"], info["department"], info["skills_idskills"])
        rows_affected = execute_query(query, params)

        return make_response(jsonify({"message": "employee added successfully", "rows_affected": rows_affected}), 201)
    except Exception as e:
        print(f"Error occurred: {e}")  # Debugging line
        return make_response(jsonify({"Error": "Internal server error"}), 500)

    
@app.route("/employees/<int:id>", methods=["PUT"])
def update_employees(id):
    try: 
        info = request.get_json()
        required_fields = ["last_name", "first_name", "age", "department", "skills_idskills"]

        if not validate_input(info, required_fields):
            return make_response(jsonify({"Error": "Missing required fields"}), 400)

        query = """UPDATE employees SET last_name = %s, first_name = %s, age = %s, department = %s, skills_idskills = %s WHERE idemployees = %s"""
        params = (info["last_name"], info["first_name"], info["age"], info["department"], info["skills_idskills"], info["street_address"], info["city"], info["country"], id)
        rows_affected = execute_query(query, params)
        return make_response(jsonify({"message": "employee updated successfully", "rows_affected": rows_affected}), 200)
    except Exception as e:
        return make_response(jsonify({"Error": "Internal server error"}), 500)
    
@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employees(id):
    try: 
        query = """DELETE FROM employees WHERE idemployees = %s"""
        params = (id,)
        rows_affected = execute_query(query, params)
        return make_response(jsonify({"message": "employee deleted successfully", "rows_affected": rows_affected}), 200)
    except Exception as e:
        return make_response(jsonify({"Error": "Internal server error"}), 500)

if __name__ == "__main__":
    app.run(debug=True)
