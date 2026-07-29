from .cafe import Cafe
from .errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            # If any friend is not vaccinated or has an expired vaccine
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # Count how many friends need to buy a mask
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
