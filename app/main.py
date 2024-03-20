from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_of_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_of_masks += 1
    if count_of_masks:
        return f"Friends should buy {count_of_masks} masks"
    return f"Friends can go to {cafe.name}"
