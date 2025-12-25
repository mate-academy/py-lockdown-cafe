from typing import Dict

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[Dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if not masks_to_buy:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {masks_to_buy} masks"
