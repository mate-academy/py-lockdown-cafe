from typing import List
from app import errors
from app.cafe import Cafe


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    mask_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.VaccineError:
            return "All friends should be vaccinated"
        except errors.NotWearingMaskError:
            mask_to_buy += 1
    if mask_to_buy:
        return f"Friends should buy {mask_to_buy} masks"

    return f"Friends can go to {cafe.name}"
