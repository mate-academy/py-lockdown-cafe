import datetime
from typing import List, Dict, Any
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError, NotVaccinatedError


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    """
    Checks if a group of friends can visit a cafe and returns a message
    indicating whether they are allowed or what the issues are.

    Args:
        friends: A list of dictionaries, where each dictionary represents
        a friend and contains information like name,
        vaccine, and wearing_a_mask.
        cafe: The Cafe object the friends want to visit.

    Returns:
        str: A message indicating whether the friends can go to the cafe.
             If not, the message specifies the reason (vaccination or masks).
    """
    masks_to_buy: int = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError:
            return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    kfc = Cafe("KFC")

    visitor1 = {
        "name": "Paul",
        "age": 23,
    }
    try:
        kfc.visit_cafe(visitor1)
    except VaccineError as e:
        print(e)

    visitor2 = {
        "name": "Paul",
        "age": 23,
        "vaccine": {
            "expiration_date": datetime.date(year=2019, month=2, day=23)
        }
    }
    try:
        kfc.visit_cafe(visitor2)
    except VaccineError as e:
        print(e)

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
        print(e)

    visitor4 = {
        "name": "Paul",
        "age": 23,
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": True
    }
    print(kfc.visit_cafe(visitor4))

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
    print(go_to_cafe(friends1, Cafe("KFC")))

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
    print(go_to_cafe(friends2, Cafe("KFC")))

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
    print(go_to_cafe(friends3, Cafe("KFC")))
