from app.cafe import visit_cafe, Cafe
from app.errors import (VaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_needed = 0

    for friend in friends:
        try:
            visit_cafe(friend)
        except NotWearingMaskError:
            mask_needed += 1
        except VaccineError:
            return "All friends should be vaccinated"

    if mask_needed == 0:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {mask_needed} masks"
