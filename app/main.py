from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_of_masks = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_of_masks += 1

    if count_of_masks:
        return f"Friends should buy {count_of_masks} masks"

    return f"Friends can go to {cafe.name}"
