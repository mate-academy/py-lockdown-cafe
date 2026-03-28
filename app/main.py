import datetime
from app.cafe import Cafe
from app.errors import (VaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    friend_not_allowed = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            friend_not_allowed += 1
        except NotWearingMaskError:
            masks_to_buy += 1

    if friend_not_allowed > 0:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"


friends = [
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
print(go_to_cafe(friends, Cafe("KFC")))
