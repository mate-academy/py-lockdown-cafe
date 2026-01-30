from __future__ import annotations

from .cafe import Cafe
from .errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    num_of_mask_needed = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            num_of_mask_needed += 1

    if num_of_mask_needed:
        return f"Friends should buy {num_of_mask_needed} masks"

    return f"Friends can go to {cafe.name}"
