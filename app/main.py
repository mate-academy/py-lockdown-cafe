# app/main.py
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            # Ловимо NotVaccinatedError та OutdatedVaccineError,
            # які наслідуються від VaccineError.
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # Ловимо помилку, коли друг не носить маску.
            masks_to_buy += 1
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    import datetime

    cafe_instance = Cafe("KFC")

    # Тест 1: Всі друзі можуть відвідати кафе
    friends1 = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
    ]
    print(go_to_cafe(friends1, cafe_instance))
    # Очікуваний результат: "Friends can go to KFC"

    # Тест 2: Друзі не носять маски
    friends2 = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False,
        },
    ]
    print(go_to_cafe(friends2, cafe_instance))
    # Очікуваний результат: "Friends should buy 2 masks"

    # Тест 3: Один друг не вакцинований
    friends3 = [
        {
            "name": "Alisa",
            "wearing_a_mask": True,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
    ]
    print(go_to_cafe(friends3, cafe_instance))
    # Очікуваний результат: "All friends should be vaccinated"
