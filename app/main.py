from .errors import VaccineError, NotWearingMaskError
from .cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    can_go = True
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except VaccineError:
            can_go = False

        except NotWearingMaskError:
            masks_to_buy += 1

    if not can_go:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
