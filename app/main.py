from app.errors import (VaccineError, NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    bolniye = []
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            bolniye.append("All friends should be vaccinated")
        except NotWearingMaskError:
            masks_to_buy += 1
            bolniye.append("wearing_a_mask")

    if "All friends should be vaccinated" in bolniye:
        return "All friends should be vaccinated"

    if "wearing_a_mask" in bolniye:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
