from typing import List

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    not_vaccinated_count = 0
    not_wearing_mask_count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_vaccinated_count += 1
        except NotWearingMaskError:
            not_wearing_mask_count += 1
    if not_vaccinated_count != 0:
        return "All friends should be vaccinated"
    if not_wearing_mask_count != 0:
        return f"Friends should buy {not_wearing_mask_count} masks"

    return f"Friends can go to {cafe.name}"
