from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = sum(
        1 for friend in friends if not friend.get("wearing_a_mask", False)
    )
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as e:
            return str(e)
        except NotWearingMaskError:
            pass

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
