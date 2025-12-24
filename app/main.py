from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    no_mask_counter = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            no_mask_counter += 1

    if no_mask_counter > 0:
        return f"Friends should buy {no_mask_counter} masks"

    return f"Friends can go to {cafe.name}"
