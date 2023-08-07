from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    needed_masks = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except NotWearingMaskError:
            needed_masks += 1
        except VaccineError:
            return "All friends should be vaccinated"

    if needed_masks:
        return f"Friends should buy {needed_masks} masks"

    return f"Friends can go to {cafe.name}"
