from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    counter_for_masks = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            counter_for_masks += 1

    if counter_for_masks:
        return f"Friends should buy {counter_for_masks} masks"

    return f"Friends can go to {cafe.name}"
