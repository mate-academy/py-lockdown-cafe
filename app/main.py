from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    NotWearingMaskError.masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as v_error:
            return str(v_error)
        except NotWearingMaskError:
            NotWearingMaskError.masks_to_buy += 1

    if NotWearingMaskError.masks_to_buy:
        return f"Friends should buy {NotWearingMaskError.masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
