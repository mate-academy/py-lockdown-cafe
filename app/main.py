from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (VaccineError, KeyError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            pass

    masks_needed = sum(1 for friend in friends
                       if not friend.get("wearing_a_mask", False))
    if masks_needed:
        return f"Friends should buy {masks_needed} masks"
    return f"Friends can go to {cafe.name}"
