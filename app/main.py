from __future__ import annotations

from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(visitor=friend)
            except VaccineError:
                raise
            except NotWearingMaskError:
                masks_to_buy += 1
                continue

    except VaccineError:
        return "All friends should be vaccinated"
    else:
        if masks_to_buy > 0:
            return f"Friends should buy {masks_to_buy} masks"
        else:
            return f"Friends can go to {cafe.name}"
