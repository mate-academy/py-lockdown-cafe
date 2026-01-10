from __future__ import annotations

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    vaccinated = True
    masks_needed = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccinated = False
            break
        except NotWearingMaskError:
            masks_needed += 1
    if not vaccinated:
        return "All friends should be vaccinated"
    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"
    return f"Friends can go to {cafe.name}"
