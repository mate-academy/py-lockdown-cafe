from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_need = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            mask_need += 1
        except VaccineError:
            return "All friends should be vaccinated"
    if mask_need:
        return f"Friends should buy {mask_need} masks"
    return f"Friends can go to {cafe.name}"
