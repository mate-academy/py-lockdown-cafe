from app.errors import VaccineError, NotWearingMaskError
from typing import List, Any


def go_to_cafe(friends: List[dict], cafe: Any) -> str:
    masks_to_buy = 0
    vaccine_issue = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_issue = True
            break
        except NotWearingMaskError:
            masks_to_buy += 1

    if vaccine_issue:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
