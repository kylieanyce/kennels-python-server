CUSTOMERS = [
    {
        "id": 2,
        "name": "Debbie Kraft",
        "address": "62 fire lane",
        "email": "debk@gmail.com"
    },
    {
        "id": 3,
        "name": "Rema Wilson",
        "address": "78 Canterbury Close",
        "email": "remaw@hotmail.com"
    },
    {
        "id": 4,
        "name": "Yolanda Carter",
        "address": "7890 Nucklehead St",
        "email": "yoliec@gmail.com"
    }
]


def get_all_customers():
    return CUSTOMERS



def get_single_customer(id):
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)