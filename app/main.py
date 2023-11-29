from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_without_masks = 0
    friends_without_vaccines = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            friends_without_vaccines += 1
        except NotWearingMaskError:
            friends_without_masks += 1
    if friends_without_vaccines:
        return "All friends should be vaccinated"
    if friends_without_masks:
        return f"Friends should buy {friends_without_masks} masks"
    return f"Friends can go to {cafe.name}"
