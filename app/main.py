from cafe import Cafe
from errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, le_cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for friend in friends:
            le_cafe.visit_cafe(friend)

    except VaccineError:
        return "Tous les amis devraient être vaccinés"
    except NotWearingMaskError:
        for friend in friends:
            if not friend.get("wearing_a_mask", True):
                masks_to_buy += 1
            return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {le_cafe.name}"
