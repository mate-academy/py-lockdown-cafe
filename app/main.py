from app.errors import (NotWearingMaskError,
                        VaccineError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_count += 1

    if mask_count > 0:
        return f"Friends should buy {mask_count} masks"
    else:
        return f"Friends can go to {cafe.name}"
