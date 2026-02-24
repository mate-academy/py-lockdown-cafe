import datetime

from app.errors import (VaccineError,
                        NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError
                        )
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError:
            return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    kfc = Cafe("KFC")
    visitor1 = {
        "name": "Paul",
        "age": 23,
    }
    try:
        kfc.visit_cafe(visitor1)
    except NotVaccinatedError as e:
        print(e.message)

    visitor2 = {
        "name": "Paul",
        "age": 23,
        "vaccine": {
            "expiration_date": datetime.date(year=2019, month=2, day=23)
        }
    }
    try:
        kfc.visit_cafe(visitor2)
    except OutdatedVaccineError as e:
        print(e.message)

    visitor3 = {
        "name": "Paul",
        "age": 23,
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": False
    }
    try:
        kfc.visit_cafe(visitor3)
    except NotWearingMaskError as e:
        print(e.message)

    visitor4 = {
        "name": "Paul",
        "age": 23,
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": True
    }
    print(kfc.visit_cafe(visitor4) == "Welcome to KFC")

    friends1 = [
        {
            "name": "Alisa",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": True
        },
        {
            "name": "Bob",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": True
        },
    ]
    print(go_to_cafe(friends1, Cafe("KFC")) == "Friends can go to KFC")

    friends2 = [
        {
            "name": "Alisa",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": False
        },
        {
            "name": "Bob",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": False
        },
    ]
    print(go_to_cafe(friends2, Cafe("KFC")) == "Friends should buy 2 masks")

    friends3 = [
        {
            "name": "Alisa",
            "wearing_a_mask": True
        },
        {
            "name": "Bob",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": True
        },
    ]
    print(
        go_to_cafe(
            friends3, Cafe("KFC")) == "All friends should be vaccinated")
