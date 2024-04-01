from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    required_masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            required_masks_to_buy += 1

    if required_masks_to_buy:
        return f"Friends should buy {required_masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
