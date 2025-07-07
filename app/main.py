from app.errors import (
    NotWearingMaskError,
    VaccineError
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask, vaccine = 0, 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine += 1
        except NotWearingMaskError:
            mask += 1
    if vaccine > 0:
        return "All friends should be vaccinated"
    if mask > 0:
        return f"Friends should buy {mask} masks"

    return f"Friends can go to {cafe.name}"
