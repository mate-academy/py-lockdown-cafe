from app.errors import (
    NotWearingMaskError,
    VaccineError
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    allowed_count = 0
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            allowed_count += 1
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError:
            return "All friends should be vaccinated"

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    if allowed_count == len(friends):
        return "Friends can go to KFC"
