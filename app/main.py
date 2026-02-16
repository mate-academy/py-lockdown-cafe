from typing import List, Dict, Any

from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    vaccine_issues = 0
    mask_issues = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_issues += 1
        except NotWearingMaskError:
            mask_issues += 1

    if vaccine_issues > 0:
        return "All friends should be vaccinated"
    elif mask_issues > 0:
        return f"Friends should buy {mask_issues} masks"

    return f"Friends can go to {cafe.name}"
