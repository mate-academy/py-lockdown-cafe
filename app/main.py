from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    unmasked_friends = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            unmasked_friends += 1
    if unmasked_friends:
        return f"Friends should buy {unmasked_friends} masks"
    else:
        return f"Friends can go to {cafe.name}"
