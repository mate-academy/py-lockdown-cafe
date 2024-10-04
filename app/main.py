from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    should_buy_mask = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            should_buy_mask += 1
    if should_buy_mask != 0:
        return f"Friends should buy {should_buy_mask} masks"
    return f"Friends can go to {cafe.name}"
