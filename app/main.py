from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends, cafe: Cafe):
    masks_to_buy = sum(1 for irresponsible_friend in friends
                       if not irresponsible_friend["wearing_a_mask"])
    try:
        for irresponsible_friend in friends:
            cafe.visit_cafe(irresponsible_friend)

    except VaccineError:
        return "All friends should be vaccinated"

    except NotWearingMaskError:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
