import datetime

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> any:
    vaccine_issue = False
    mask_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_issue = True
        except NotWearingMaskError:
            mask_to_buy += 1

    if vaccine_issue:
        return "All friends should be vaccinated"
    elif mask_to_buy > 0:
        return f"Friends should buy {mask_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"


friends = [
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
