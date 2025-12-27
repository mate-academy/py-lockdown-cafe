from typing import List
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    any_vaccine_error = False  # Add a flag

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            any_vaccine_error = True  # Set flag on VaccineError
        except NotWearingMaskError:
            masks_to_buy += 1

    if any_vaccine_error:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
