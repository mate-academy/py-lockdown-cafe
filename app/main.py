import datetime
from typing import List
from .cafe import Cafe
from .errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                masks_to_buy += 1
    except VaccineError:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    # Приклад використання
    kfc = Cafe("KFC")
    friends_list = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False
        },
    ]

    print(go_to_cafe(friends_list, kfc))
