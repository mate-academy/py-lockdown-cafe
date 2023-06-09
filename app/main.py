from __future__ import annotations


from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    no_vaccine = False
    no_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            no_vaccine = True
            break
        except NotWearingMaskError:
            no_mask += 1

    if no_vaccine:
        return "All friends should be vaccinated"
    elif no_mask:
        return f"Friends should buy {no_mask} masks"
    return "Friends can go to KFC"
