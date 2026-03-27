from __future__ import annotations
from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str | VaccineError:
    unmasked = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            unmasked += 1
    if unmasked >= 1:
        return f"Friends should buy {unmasked} masks"
    return f"Friends can go to {cafe.name}"
