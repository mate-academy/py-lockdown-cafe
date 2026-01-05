from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_wear_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            not_wear_mask += 1

    if not_wear_mask:
        return f"Friends should buy {not_wear_mask} masks"
    return f"Friends can go to {cafe.name}"
