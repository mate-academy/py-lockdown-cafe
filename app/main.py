from app.cafe import Cafe

from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    needed_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            needed_masks += 1
    if needed_masks:
        return f"Friends should buy {needed_masks} masks"
    return "Friends can go to KFC"
