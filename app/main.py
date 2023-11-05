from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_counter = 0

    for friend in friends:
        try:
            cafe.visit_cafe(visitor=friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_counter += 1

    if masks_counter:
        return f"Friends should buy {masks_counter} masks"

    return f"Friends can go to {cafe.name}"
