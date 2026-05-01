from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_needed = sum(
        1 for friend in friends
        if not friend.get("wearing_a_mask", False))

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            pass

    if masks_needed:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"
