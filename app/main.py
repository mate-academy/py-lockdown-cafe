from .errors import VaccineError, NotWearingMaskError
from .cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    result = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            if cafe.visit_cafe(friend) == f"Welcome to {cafe.name}":
                result += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
