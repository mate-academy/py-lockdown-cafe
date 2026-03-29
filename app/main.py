from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_error = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_error += 1
    if mask_error != 0:
        return f"Friends should buy {mask_error} masks"
    return f"Friends can go to {cafe.name}"
