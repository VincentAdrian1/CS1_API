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

logging.basicConfig(level=logging.ERROR)

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


@app.route('/')
def employees():
    try:
       query = """Select concat(employees.first_name, " ", employees.last_name) as Full_Name, 
                        idemployees, age, department, skills_idskills FROM employees"""
       data = data_fetch(query)
       return make_response(jsonify(data), 200)
    except Exception as e:
        return make_response(jsonify({"success": False, "error": str(e)}))


if __name__ == "__main__":
    app.run(debug=True)
