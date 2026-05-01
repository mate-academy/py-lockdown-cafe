from app.cafe import Cafe
from app.errors import (
    NotWearingMaskError,
    VaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    check = True
    mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            check = False
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            check = False
            mask += 1
    if check:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {mask} masks"
