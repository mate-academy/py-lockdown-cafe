from __future__ import annotations
from app.cafe import Cafe
import app.errors as error


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except error.VaccineError:
            return "All friends should be vaccinated"
        except error.NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
