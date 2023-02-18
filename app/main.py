from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    without_masks = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except (KeyError, VaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            without_masks += 1
    if without_masks:
        return f"Friends should buy {without_masks} masks"
    return f"Friends can go to {cafe.name}"
