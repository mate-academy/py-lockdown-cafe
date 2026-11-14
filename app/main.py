from app.cafe import Cafe
from app.errors import (NotWearingMaskError, VaccineError)


VisitorData = dict


def go_to_cafe(friends: list[VisitorData], cafe: Cafe) -> str:
    no_wearing_mask_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            no_wearing_mask_count += 1
    return f"Friends should buy {no_wearing_mask_count} masks"  \
        if no_wearing_mask_count else f"Friends can go to {cafe.name}"
