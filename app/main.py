from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    all_ok = 0
    masks_to_buy = 0
    should_to_vaccinate = False
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            all_ok += 1
        except VaccineError:
            should_to_vaccinate = True
        except NotWearingMaskError:
            masks_to_buy += 1
    if should_to_vaccinate:
        return f"{VaccineError()}"
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
