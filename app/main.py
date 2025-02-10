from app.cafe import Cafe, Visitor
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[Visitor], cafe: Cafe) -> str:
    mask_to_buy = 0

    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_to_buy += 1

    if mask_to_buy:
        return f"Friends should buy {mask_to_buy} masks"

    return f"Friends can go to {cafe.name}"
