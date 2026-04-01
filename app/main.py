from app.cafe import Cafe
from app.errors import (NotWearingMaskError, VaccineError)


def go_to_cafe(friends: dict, cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as err:
            return VaccineError.__str__(err)
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy:
        return NotWearingMaskError(masks_to_buy).__str__()
    return f"Friends can go to {cafe.name}"
