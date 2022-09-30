from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                masks_to_buy += 1
            except VaccineError:
                raise
    except VaccineError as e:
        message = ''.join(list(e.args))
        return message
    else:
        if masks_to_buy != 0:
            return f"Friends should buy {masks_to_buy} masks"
        return "Friends can go to KFC"
