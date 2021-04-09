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

def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal

def delete_animal(id):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)