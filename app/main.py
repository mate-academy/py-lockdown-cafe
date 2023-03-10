from app.cafe import Cafe
from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_to_buy_counter = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_to_buy_counter += 1
    if mask_to_buy_counter > 0:
        return f"Friends should buy {mask_to_buy_counter} masks"
    return f"Friends can go to {cafe.name}"
