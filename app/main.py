from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_needed = 0
    message = f"Friends can go to {cafe.name}"
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_needed += 1
    if masks_needed:
        message = f"Friends should buy {masks_needed} masks"
    return message
