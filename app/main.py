import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_needed = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_needed += 1

    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"


# Приклади використання
if __name__ == "__main__":
    kfc = Cafe("KFC")

    # Тест 1: всі друзі можуть піти в кафе
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
    print(go_to_cafe(friends1, kfc))  # Виведе: Friends can go to KFC

    # Тест 2: відсутність масок
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
    print(go_to_cafe(friends2, kfc))  # Виведе: Friends should buy 2 masks

    # Тест 3: відсутність вакцинації
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
    print(go_to_cafe(friends3, kfc))
