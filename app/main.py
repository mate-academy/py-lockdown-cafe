from typing import List

from app.cafe import Cafe
from app.models.visitor import Visitor
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[Visitor], cafe: Cafe) -> str:
    no_mask_friends = 0
    no_vaccine_friends = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            no_vaccine_friends += 1
        except NotWearingMaskError:
            no_mask_friends += 1

    if no_vaccine_friends > 0:
        return "All friends should be vaccinated"

    if no_mask_friends > 0:
        return f"Friends should buy {no_mask_friends} masks"

    return f"Friends can go to {cafe.name}"
