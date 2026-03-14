from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks = 0
    vaccin = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccin += 1
        except NotWearingMaskError:
            masks += 1
    if vaccin:
        return "All friends should be vaccinated"
    if masks:
        return f"Friends should buy {masks} masks"
    return f"Friends can go to {cafe.name}"
