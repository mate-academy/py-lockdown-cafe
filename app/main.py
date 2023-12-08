from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    control = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            control += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    if control == len(friends):
        return f"Friends can go to {cafe.name}"
