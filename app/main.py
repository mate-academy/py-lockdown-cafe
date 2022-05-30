from app.errors import (
    NotWearingMaskError,
    VaccineError
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe):
    persons_without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            persons_without_mask += 1
    if persons_without_mask > 0:
        return f"Friends should buy {persons_without_mask} masks"
    return f"Friends can go to {cafe.name}"
