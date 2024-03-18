from typing import List, Dict
from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: List[Dict], cafe: Cafe) -> str:
    mask_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            continue
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            mask_to_buy += 1
            continue
    if mask_to_buy > 0:
        return f"Friends should buy {mask_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
