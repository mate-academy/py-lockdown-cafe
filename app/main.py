from __future__ import annotations

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_error = 0
    mask_error = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            vaccine_error += 1
        except NotWearingMaskError:
            mask_error += 1
    if vaccine_error:
        return "All friends should be vaccinated"
    if mask_error:
        return f"Friends should buy {mask_error} masks"
    return f"Friends can go to {cafe.name}"
