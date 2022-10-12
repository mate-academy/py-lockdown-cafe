from __future__ import annotations

from .cafe import Cafe
from .errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_to_ok = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            _ = cafe.visit_cafe(friend)
            friends_to_ok += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if friends_to_ok == len(friends):
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {masks_to_buy} masks"
