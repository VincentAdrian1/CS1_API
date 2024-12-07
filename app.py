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

@app.route('/')
def index():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM employees")
        employees = cur.fetchall()
        cur.close()

        return make_response(jsonify({"success": True, "employees": employees}), 200)
    except Exception as e:
        return make_response(jsonify({"success": False, "error": str(e)}), 500)


if __name__ == "__main__":
    app.run(debug=True)
