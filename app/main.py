from .cafe import Cafe
from .errors import (VaccineError,
                     NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> (None, str):
    masks_to_buy = sum(1 for j in friends if not j["wearing_a_mask"])
    is_mask = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            is_mask = False

    if not is_mask:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
