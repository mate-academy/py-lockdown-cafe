from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_counter = 0
    masks_need = len(friends)
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            masks_counter += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            pass
    if masks_counter == masks_need:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {masks_need - masks_counter} masks"
