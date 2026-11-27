from typing import Any

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(
        friends: list[dict[str, Any]],
        cafe: Cafe
) -> str:
    not_a_vaccine = False
    mask_to_by = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            mask_to_by += 1
        except VaccineError:
            not_a_vaccine = True
    if not_a_vaccine:
        return "All friends should be vaccinated"
    if mask_to_by:
        return f"Friends should buy {mask_to_by} masks"
    return f"Friends can go to {cafe.name}"
