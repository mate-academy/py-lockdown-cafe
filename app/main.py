from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: dict, cafe: Cafe) -> str:
    counter_without_mask = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            counter_without_mask += 1

    if counter_without_mask:
        return f"Friends should buy {counter_without_mask} masks"

    return f"Friends can go to {cafe.name}"
