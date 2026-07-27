from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccines = 0
    mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            mask += 1
        except VaccineError:
            vaccines += 1

    if vaccines:
        return "All friends should be vaccinated"
    if mask:
        return (f"Friends should buy {mask} masks")
    return f"Friends can go to {cafe.name}"
