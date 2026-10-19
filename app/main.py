from app.cafe.cafe import Cafe
from app.errors import errors


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_counter = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.VaccineError:
            return "All friends should be vaccinated"
        except errors.NotWearingMaskError:
            mask_counter += 1
    if mask_counter > 0:
        return f"Friends should buy {mask_counter} masks"
    return f"Friends can go to {cafe.name}"
