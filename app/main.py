import datetime
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy, valid_vacine = 0, 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            valid_vacine += 1
        except NotWearingMaskError:
            masks_to_buy += 1

    if valid_vacine:
        return "All friends should be vaccinated"

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    friends = [
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
                "expiration_date": datetime.date(2019, 2, 22)
            },
            "wearing_a_mask": False
        },
    ]
    print(go_to_cafe(friends, Cafe("KFC")))
