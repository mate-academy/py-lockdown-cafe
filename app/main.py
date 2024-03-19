from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    need_masks = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            need_masks += 1
    if need_masks:
        return f"Friends should buy {need_masks} masks"
    return f"Friends can go to {cafe.name}"
