from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    havent_masks = []
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            havent_masks.append(False)

    if len(havent_masks) > 0:
        return f"Friends should buy {len(havent_masks)} masks"

    return f"Friends can go to {cafe.name}"
