from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_counter = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as e:
            return f"{e}"
        except NotWearingMaskError:
            masks_counter += 1
    if masks_counter:
        return f"Friends should buy {masks_counter} masks"
    return f"Friends can go to {cafe.name}"
