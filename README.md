# 📝 Task Manager (Full Stack Project)

## 📌 Overview

This project is a full-stack Task Management application where users can add, update, and delete tasks.
It demonstrates how frontend, backend, and database systems work together in a real-world application.

---

## 🚀 Features

* Add new tasks
* Update task status (Pending → Completed)
* Delete tasks
* Dynamic task list updates

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Database:** Oracle Database
* **Frontend:** HTML, CSS, JavaScript

---

## ⚙️ How to Run

### 🔹 1. Start Backend

```bash
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

### 🔹 2. Start Frontend

```bash
python -m http.server 5500
```

Open in browser:

```
http://localhost:5500/index.html
```

---

## 🔗 API Endpoints

| Method | Endpoint    | Description        |
| ------ | ----------- | ------------------ |
| GET    | /tasks      | Get all tasks      |
| POST   | /tasks      | Add new task       |
| PUT    | /tasks/{id} | Update task status |
| DELETE | /tasks/{id} | Delete task        |

---

## 🗄️ Database Setup (Oracle)

Run the following SQL:

```sql
CREATE TABLE tasks (
    id NUMBER PRIMARY KEY,
    title VARCHAR2(255),
    status VARCHAR2(50)
);

CREATE SEQUENCE task_seq START WITH 1 INCREMENT BY 1;
```

---

## 🎯 Learning Outcomes

* Built REST APIs using Flask
* Integrated Oracle Database
* Performed CRUD operations
* Connected frontend with backend

---

## 👨‍💻 Author

Gumma Guru Prasanna
