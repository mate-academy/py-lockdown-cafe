from typing import List, Dict, Any
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    vaccine_error = False
    mask_missing = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_error = True
        except NotWearingMaskError:
            mask_missing += 1
    if vaccine_error:
        return "All friends should be vaccinated"
    if mask_missing:
        return f"Friends should buy {mask_missing} masks"
    return f"Friends can go to {cafe.name}"
