from app.cafe import Cafe
from app.errors import (NotWearingMaskError, VaccineError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    mask_to_by = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_to_by += 1
    if mask_to_by:
        return f"Friends should buy {mask_to_by} masks"
    return f"Friends can go to {cafe.name}"
