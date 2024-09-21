from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: dict, cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccinated = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccinated = False
        except NotWearingMaskError:
            masks_to_buy += 1
    if not vaccinated:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
