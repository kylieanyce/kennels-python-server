import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {
        "id": 1,
        "name": "Teresa May",
        "location_id": 3
    },
    {
        "id": 2,
        "name": "Meriweather Pavillion",
        "location_id": 2
    },
    {
        "id": 3,
        "name": "Geri Mander",
        "location_id": 2
    },
    {
        "id": 4,
        "name": "Amanda Blevy",
        "location_id": 1
    },
    {
        "name": "Marge Barge",
        "location_id": 3,
        "id": 5
    }
]

def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.email,
            e.location_id
        FROM employee e
        """)

        employees = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['email'], row['location_id'])
            employees.append(employee.__dict__)
    return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.email,
            e.location_id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()
        employee = Employee(data['id'], data['name'], data['address'],
                            data['email'], data['location_id'])
        return json.dumps(employee.__dict__)


def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee


def delete_employee(id):
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Update the value.
            EMPLOYEES[index] = new_employee
            break