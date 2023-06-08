from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            continue
        except VaccineError:
            return "All friends should be vaccinated"

    without_mask = 0

    for friend in friends:
        if not friend.get("wearing_a_mask", False):
            without_mask += 1

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            return f"Friends should buy {without_mask} masks"

    return f"Friends can go to {cafe.name}"
