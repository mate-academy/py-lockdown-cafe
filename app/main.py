import datetime
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    """
    Повертає повідомлення про те, чи можуть друзі піти в кафе.

    Якщо хтось не вакцинований — повертає помилку.
    Якщо хтось без маски — рахує, скільки потрібно купити масок.
    """
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"


# === Тести ===
if __name__ == "__main__":
    today = datetime.date.today()

    friends1 = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": today},
            "wearing_a_mask": True,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": today},
            "wearing_a_mask": True,
        },
    ]
    print(go_to_cafe(friends1, Cafe("KFC")))

    friends2 = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": today},
            "wearing_a_mask": False,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": today},
            "wearing_a_mask": False,
        },
    ]
    print(go_to_cafe(friends2, Cafe("KFC")))

    friends3 = [
        {
            "name": "Alisa",
            "wearing_a_mask": True,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": today},
            "wearing_a_mask": True,
        },
    ]
    print(go_to_cafe(friends3, Cafe("KFC")))

    friends4 = [
        {
            "name": "Alisa",
            "vaccine": {
                "expiration_date": datetime.date(2019, 2, 23)
            },
            "wearing_a_mask": True,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": today},
            "wearing_a_mask": True,
        },
    ]
    print(go_to_cafe(friends4, Cafe("KFC")))
