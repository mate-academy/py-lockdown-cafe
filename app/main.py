from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    buy_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            buy_mask += 1
    if buy_mask:
        return f"Friends should buy {buy_mask} masks"
    return f"Friends can go to {cafe.name}"
