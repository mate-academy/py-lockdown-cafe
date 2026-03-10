from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            pass
    masks_to_buy = sum(
        1 for friend in friends if not friend.get("wearing_a_mask")
    )
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
