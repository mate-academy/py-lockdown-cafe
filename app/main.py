from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    is_good = True
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            is_good = False
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            is_good = False
            masks_to_buy += 1
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    if is_good is True:
        return f"Friends can go to {cafe.name}"
