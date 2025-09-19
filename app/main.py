import datetime

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy: int = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    cafe = Cafe("KFC")

    friends_all_good = [
        {
            "name": "Alice",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
    ]
    print(go_to_cafe(friends_all_good, cafe))

    friends_no_mask = [
        {
            "name": "Alice",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False,
        },
    ]
    print(go_to_cafe(friends_no_mask, cafe))

    friends_not_vaccinated = [
        {"name": "Alice", "wearing_a_mask": True},
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
    ]
    print(go_to_cafe(friends_not_vaccinated, cafe))
