from app.errors import (VaccineError, NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    increment_counter = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            increment_counter += 1
    if increment_counter > 0:
        return f"Friends should buy {increment_counter} masks"
    return f"Friends can go to {cafe.name}"
