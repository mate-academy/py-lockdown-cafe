from __future__ import annotations
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    mask_error_counter = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_error_counter += 1
    if mask_error_counter:
        return f"Friends should buy {mask_error_counter} masks"

    return f"Friends can go to {cafe.name}"
