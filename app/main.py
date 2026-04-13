from typing import Any


from app.errors import (
    VaccineError,
    NotWearingMaskError
)
from app.cafe import Cafe


def go_to_cafe(friends: list[dict[str, Any]], cafe: Cafe) -> str:
    mask_amount = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_amount += 1

    if mask_amount:
        return f"Friends should buy {mask_amount} masks"
    return f"Friends can go to {cafe.name}"
