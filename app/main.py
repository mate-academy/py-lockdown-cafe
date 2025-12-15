from typing import List
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    """
    Check if all friends can go to the cafe.

    :param friends: list of visitors
    :param cafe: Cafe instance
    :return: message string
    """
    masks_to_buy = 0

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
    import datetime

    friends = [
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
    print(go_to_cafe(friends, Cafe("KFC")))
