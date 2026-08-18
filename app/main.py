from app.errors import (VaccineError, NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    no_mask_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            no_mask_count += 1
    if no_mask_count:
        return f"Friends should buy {no_mask_count} masks"
    return f"Friends can go to {cafe.name}"
