from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_mask_for_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_mask_for_buy += 1

    if count_mask_for_buy:
        return f"Friends should buy {count_mask_for_buy} masks"
    return f"Friends can go to {cafe.name}"
