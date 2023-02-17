from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    result = ""

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError as e:
            result = str(e)

    if masks_to_buy and not result:
        result = f"Friends should buy {masks_to_buy} masks"

    return result or f"Friends can go to {cafe.name}"
