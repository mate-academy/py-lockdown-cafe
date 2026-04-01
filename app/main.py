from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    # Count friends without masks — we need this for the mask message
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            # Friend is vaccinated but has no mask — count it
            masks_to_buy += 1

    # If we get here — no vaccine problems found
    # Check if anyone needed a mask
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
