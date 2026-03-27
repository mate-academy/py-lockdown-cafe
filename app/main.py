from app.errors import (
    VaccineError,
    NotWearingMaskError
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    without_mask = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            masks_to_buy += 1
            without_mask = True

    if without_mask:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
