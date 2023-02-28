from app.cafe import Cafe
from app.errors import (VaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks += 1
        except VaccineError:
            return "All friends should be vaccinated"
    if masks:
        return f"Friends should buy {masks} masks"
    return f"Friends can go to {cafe.name}"
