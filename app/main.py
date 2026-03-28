from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    flag = f"Friends can go to {cafe.name}"
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    return (
        flag
        if not masks_to_buy
        else f"Friends should buy {masks_to_buy} masks"
    )
