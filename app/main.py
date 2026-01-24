from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 1:
        return f"Friends should buy {masks_to_buy} masks"
    elif masks_to_buy == 1:
        return "Friends should buy 1 mask"

    return f"Friends can go to {cafe.name}"
