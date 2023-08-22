import app.errors as errors
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_nedeed = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.VaccineError as e:
            return str(e)
        except errors.NotWearingMaskError:
            masks_nedeed += 1

    if masks_nedeed:
        return f"Friends should buy {masks_nedeed} masks"

    return f"Friends can go to {cafe.name}"
