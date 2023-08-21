from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    buy_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            buy_masks += 1
        except VaccineError:
            return "All friends should be vaccinated"

    if buy_masks:
        return f"Friends should buy {buy_masks} masks"

    return f"Friends can go to {cafe.name}"
