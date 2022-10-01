from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError as e:
            return str(e)

    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"
    return "Friends can go to KFC"
