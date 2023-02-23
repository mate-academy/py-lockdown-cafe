from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    mask_needed_counter = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_needed_counter += 1
    if mask_needed_counter == 0:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {mask_needed_counter} masks"
