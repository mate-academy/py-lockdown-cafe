from typing import List, Dict, Any
from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    vaccinated_issues: int = 0
    mask_issues: int = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccinated_issues += 1
        except NotWearingMaskError:
            mask_issues += 1

    if vaccinated_issues > 0:
        return "All friends should be vaccinated"
    elif mask_issues > 0:
        return f"Friends should buy {mask_issues} masks"
    else:
        return f"Friends can go to {cafe.name}"