from typing import List, Dict

from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: List[Dict], cafe: Cafe) -> str:
    masks_needed: int = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_needed += 1
    if masks_needed:
        return f"Friends should buy {masks_needed} masks"
    return f"Friends can go to {cafe.name}"
