from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_counter = 0
    mask_counter = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_counter += 1
        except NotWearingMaskError:
            mask_counter += 1

    if vaccine_counter > 0:
        return "All friends should be vaccinated"
    if mask_counter > 0:
        return f"Friends should buy {mask_counter} masks"
    return f"Friends can go to {cafe.name}"
