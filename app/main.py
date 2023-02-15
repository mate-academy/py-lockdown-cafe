from app.cafe import Cafe
from app.errors import (
    NotWearingMaskError,
    VaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccine_flag = False
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError:
            vaccine_flag = True
    if vaccine_flag:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
