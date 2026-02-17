"""Main module implementing go_to_cafe function."""

from __future__ import annotations
from typing import List, Dict, Any
from cafe import Cafe
from errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    """
    Check if a group of friends can go to the cafe.

    Args:
        friends: List of dictionaries with friends' info.
        cafe: Cafe instance to visit.

    Returns:
        str: Message about group access.
    """
    masks_needed = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_needed += 1

    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"
