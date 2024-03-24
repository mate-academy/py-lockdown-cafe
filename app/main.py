from typing import List, Dict

from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: List[Dict], cafe: Cafe) -> str:
    not_all_vaccinated = False
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_all_vaccinated = True
        except NotWearingMaskError:
            masks_to_buy += 1

    if not_all_vaccinated:
        return "All friends should be vaccinated"
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
