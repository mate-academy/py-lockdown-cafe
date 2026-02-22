from errors import VaccineError, NotWearingMaskError
from cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_needed = 0
    all_vaccinated = True

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            all_vaccinated = False
        except NotWearingMaskError:
            masks_needed += 1

        if not friend.get("wearing_a_mask", False):
            masks_needed += 1

    if not all_vaccinated:
        return "All friends should be vaccinated"

    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"


import datetime

friends = [
    {
        "name": "Alice",
        "vaccine": {"expiration_date": datetime.date.today()},
        "wearing_a_mask": True
    },
    {
        "name": "Bob",
        "vaccine": {"expiration_date": datetime.date.today()},
        "wearing_a_mask": False
    }
]

cafe = Cafe("KFC")
print(go_to_cafe(friends, cafe))
