from typing import List, Dict
from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: List[Dict], cafe: Cafe) -> str:
    """Determines if a group of friends can visit a cafe together."""
    mask_needed: int = 0
    all_vaccinated: bool = True

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            all_vaccinated = False
        except NotWearingMaskError:
            mask_needed += 1

    if not all_vaccinated:
        return "All friends should be vaccinated"
    if mask_needed:
        return f"Friends should buy {mask_needed} masks"
    return f"Friends can go to {cafe.name}"

