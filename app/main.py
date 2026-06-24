from typing import List

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    errors = {
        "not_wearing_mask": 0
    }

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            errors["not_wearing_mask"] += 1

    if errors["not_wearing_mask"]:
        return f"Friends should buy {errors['not_wearing_mask']} masks"

    return f"Friends can go to {cafe.name}"
