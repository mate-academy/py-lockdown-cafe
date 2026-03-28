import datetime
from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError,
                        NotVaccinatedError, OutdatedVaccineError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccine_issues = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_issues = True
        except NotWearingMaskError:
            masks_to_buy += 1

    if vaccine_issues:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
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
        print(f"Test 1 passed: {e}")

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
        print(f"Test 2 passed: {e}")

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
        print(f"Test 3 passed: {e}")

    visitor4 = {
        "name": "Paul",
        "age": 23,
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": True
    }
    result = kfc.visit_cafe(visitor4)
    print(f"Test 4: {result}")
    assert result == "Welcome to KFC"

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
    result = go_to_cafe(friends1, kfc)
    print(f"Test 5: {result}")
    assert result == "Friends can go to KFC"

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
    result = go_to_cafe(friends2, kfc)
    print(f"Test 6: {result}")
    assert result == "Friends should buy 2 masks"

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
    result = go_to_cafe(friends3, kfc)
    print(f"Test 7: {result}")
    assert result == "All friends should be vaccinated"

    print("All tests passed!")
