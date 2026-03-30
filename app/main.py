from __future__ import annotations
from typing import List

from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: List, cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccinated = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccinated = False
        except NotWearingMaskError:
            masks_to_buy += 1
    if not vaccinated:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
