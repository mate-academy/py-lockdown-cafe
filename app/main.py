from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    amount_of_masks = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            amount_of_masks += 1

    if amount_of_masks:
        return f"Friends should buy {amount_of_masks} masks"

    return f"Friends can go to {cafe.name}"
