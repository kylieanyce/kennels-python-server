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
    return EMPLOYEES


def get_single_employee(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee


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