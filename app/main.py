from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_counter = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_counter += 1
    if masks_counter == 0:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {masks_counter} masks"
