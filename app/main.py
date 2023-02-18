from typing import List
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    errors_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            errors_count += 1
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
            errors_count += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
