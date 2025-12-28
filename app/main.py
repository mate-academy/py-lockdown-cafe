from typing import List, Dict, Any

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    """Decide whether a group of friends can visit `cafe`.

    The function handles exceptions internally using `try/except` and never
    propagates `VaccineError` or `NotWearingMaskError` to callers.

    Args:
        friends: List of visitor dictionaries accepted by `Cafe.visit_cafe`.
        cafe: Instance of `Cafe` to validate visits against.

    Returns:
        A string message describing whether and under what conditions the
        friends can visit the cafe.
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
