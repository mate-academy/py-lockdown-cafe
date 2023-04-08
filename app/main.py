from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: dict, cafe: Cafe) -> str:
    buy_to_mask = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except NotWearingMaskError:
            buy_to_mask += 1
        except VaccineError:
            return "All friends should be vaccinated"
    if buy_to_mask > 0:
        return f"Friends should buy {buy_to_mask} masks"
    return f"Friends can go to {cafe.name}"
