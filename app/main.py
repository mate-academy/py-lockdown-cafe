from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_without_masks = []
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            friends_without_masks.append(friend)

    if friends_without_masks:
        return f"Friends should buy {len(friends_without_masks)} masks"

    return f"Friends can go to {cafe.name}"
