from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    mask_counter = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                mask_counter += 1
    except VaccineError:
        return "All friends should be vaccinated"
    if mask_counter > 0:
        return f"Friends should buy {mask_counter} masks"
    return f"Friends can go to {cafe.name}"
