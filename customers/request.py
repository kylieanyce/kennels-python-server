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
