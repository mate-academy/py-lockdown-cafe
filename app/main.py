from __future__ import annotations
from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    error = 0
    for friend in friends:
        try:
            try:
                cafe.visit_cafe(friend)
            except VaccineError:
                error += 1
                return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
            error += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    if error == 0:
        return f"Friends can go to {cafe.name}"
