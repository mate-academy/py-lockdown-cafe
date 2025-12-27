# main.py
from __future__ import annotations

from typing import List, Dict, Any

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    masks_needed = 0
    all_vaccinated_ok = True

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            all_vaccinated_ok = False
        except NotWearingMaskError:
            masks_needed += 1

    if not all_vaccinated_ok:
        return "All friends should be vaccinated"
    if masks_needed:
        return f"Friends should buy {masks_needed} masks"
    return f"Friends can go to {cafe.name}"
