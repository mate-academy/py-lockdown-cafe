from .cafe import Cafe
from .errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    missing_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            missing_masks += 1
    if not missing_masks:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {missing_masks} masks"
