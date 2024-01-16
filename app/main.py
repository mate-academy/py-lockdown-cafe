from __future__ import annotations
from .cafe import Cafe
from .errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    mask_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            mask_count += 1
        except VaccineError:
            return "All friends should be vaccinated"
    if mask_count != 0:
        return f"Friends should buy {mask_count} masks"
    return f"Friends can go to {cafe.name}"
