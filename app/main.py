from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            pass
        except VaccineError:
            return "All friends should be vaccinated"

    masks_needed = sum(
        1 for friend in friends
        if friend["wearing_a_mask"] is not True
    )

    if masks_needed:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"
