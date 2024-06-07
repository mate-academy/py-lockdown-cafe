from app.errors import (
    NotWearingMaskError,
    VaccineError
)

from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_not_worn = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_not_worn += 1

    if masks_not_worn:
        return f"Friends should buy {masks_not_worn} masks"

    return f"Friends can go to {cafe.name}"
