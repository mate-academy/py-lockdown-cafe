from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    not_wearing_masks = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except NotWearingMaskError:
            not_wearing_masks += 1
        except VaccineError:
            return "All friends should be vaccinated"
    if not not_wearing_masks:
        return "Friends can go to KFC"
    return f"Friends should buy {not_wearing_masks} masks"
