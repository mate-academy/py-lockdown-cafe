from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    unmasked_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            unmasked_count += 1
    if unmasked_count:
        return f"Friends should buy {unmasked_count} masks"
    return f"Friends can go to {cafe.name}"
