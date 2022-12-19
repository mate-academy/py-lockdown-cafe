from __future__ import annotations
from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str | VaccineError:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            continue

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            unmasked = 0
            for some_friend in friends:
                if some_friend["wearing_a_mask"] is False:
                    unmasked += 1
            return f"Friends should buy {unmasked} masks"
    return f"Friends can go to {cafe.name}"
