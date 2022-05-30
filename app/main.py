from app.errors import (
    NotWearingMaskError,
    VaccineError
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe):
    people_without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            people_without_mask += 1
    if people_without_mask > 0:
        return f"Friends should buy {people_without_mask} masks"
    return f"Friends can go to {cafe.name}"
