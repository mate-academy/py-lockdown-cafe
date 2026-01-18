from typing import List

from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    num_of_errors = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            num_of_errors += 1
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0 and num_of_errors == 0:
        return f"Friends should buy {masks_to_buy} masks"
    if num_of_errors == 0:
        return f"Friends can go to {cafe.name}"
    else:
        return "All friends should be vaccinated"
