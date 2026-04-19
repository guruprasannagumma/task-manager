from flask import Flask, request, jsonify
from flask_cors import CORS
import cx_Oracle

app = Flask(__name__)

# ✅ Proper CORS (allow all origins)
CORS(app, resources={r"/*": {"origins": "*"}})
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
conn = cx_Oracle.connect(user="system", password="manager", dsn=dsn)
cursor = conn.cursor()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    return jsonify([{"id": r[0], "title": r[1], "status": r[2]} for r in rows])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    cursor.execute(
        "INSERT INTO tasks (id, title, status) VALUES (task_seq.NEXTVAL, :1, :2)",
        (data['title'], "Pending")
    )
    conn.commit()
    return jsonify({"msg": "added"})

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.json
    cursor.execute("UPDATE tasks SET status=:1 WHERE id=:2", (data['status'], id))
    conn.commit()
    return jsonify({"msg": "updated"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    cursor.execute("DELETE FROM tasks WHERE id=:1", (id,))
    conn.commit()
    return jsonify({"msg": "deleted"})

app.run(debug=True)