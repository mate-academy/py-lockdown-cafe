from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            # Try to visit the cafe for each friend
            cafe.visit_cafe(friend)
        except VaccineError:
            # If the friend is not vaccinated or has an outdated vaccine
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # If the friend is not wearing a mask,
            # count how many masks are needed
            masks_to_buy += 1

    # If some friends are not wearing masks
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    # All friends are allowed to go to the cafe
    return f"Friends can go to {cafe.name}"
