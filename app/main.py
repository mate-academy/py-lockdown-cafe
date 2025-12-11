from app.cafe import Cafe

from app.errors import (
    NotWearingMaskError,
    VaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_without_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            friends_without_masks += 1

    if friends_without_masks:
        return f"Friends should buy {friends_without_masks} masks"

    return f"Friends can go to {cafe.name}"
