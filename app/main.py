from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_mask_needed = 0
    for friend in friends:

        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_mask_needed += 1

    if count_mask_needed:
        return f"Friends should buy {count_mask_needed} masks"

    return f"Friends can go to {cafe.name}"
