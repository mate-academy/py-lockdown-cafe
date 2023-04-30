from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    visitor_can_go_to_cafe = 0
    count_masks = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_masks += 1
        else:
            visitor_can_go_to_cafe += 1
    if visitor_can_go_to_cafe == len(friends):
        return f"Friends can go to {cafe.name}"
    if count_masks > 0:
        return f"Friends should buy {count_masks} masks"
