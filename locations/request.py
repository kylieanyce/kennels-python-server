LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    },
    {
        "name": "Nashville Southwest",
        "id": 3,
        "address": "300 Old Town Rd"
    }
]


def get_all_locations():
    return LOCATIONS



def get_single_location(id):
    requested_location = None
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    return requested_location
