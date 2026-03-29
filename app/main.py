from .cafe import Cafe
from .errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    lacking_masks = 0

    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            lacking_masks += 1

    if lacking_masks:
        return f"Friends should buy {lacking_masks} masks"

    return f"Friends can go to {cafe.name}"
