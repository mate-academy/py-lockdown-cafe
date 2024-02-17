from __future__ import annotations

from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_problems = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_problems = 1
        except NotWearingMaskError:
            masks_to_buy += 1
    if not vaccine_problems and not masks_to_buy:
        return f"Friends can go to {cafe.name}"
    if vaccine_problems:
        return "All friends should be vaccinated"
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
