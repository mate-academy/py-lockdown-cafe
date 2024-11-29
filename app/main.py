from __future__ import annotations
import app.errors
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except app.errors.NotWearingMaskError:
                masks_to_buy += 1
    except app.errors.VaccineError:
        return "All friends should be vaccinated"
    else:
        if masks_to_buy:
            return f"Friends should buy {masks_to_buy} masks"
        else:
            return f"Friends can go to {cafe.name}"
