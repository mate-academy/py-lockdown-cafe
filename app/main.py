from __future__ import annotations

from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    access_granted = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            access_granted = False
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            access_granted = False
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    if access_granted:
        return f"Friends can go to {cafe.name}"
