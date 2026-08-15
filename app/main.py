from .errors import (VaccineError, NotWearingMaskError)
from .cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    someone_with_no_mask = False
    no_mask_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            someone_with_no_mask = True
            no_mask_count += 1
    if someone_with_no_mask:
        return f"Friends should buy {no_mask_count} masks"
    return f"Friends can go to {cafe.name}"
