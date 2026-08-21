from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    is_good = True
    masks_to_buy = 0
    vaccination_error = False
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            is_good = False
            vaccination_error = True
        except NotWearingMaskError:
            is_good = False
            masks_to_buy += 1
    if vaccination_error:
        return ("All friends should be vaccinated")
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    if is_good:
        return f"Friends can go to {cafe.name}"
