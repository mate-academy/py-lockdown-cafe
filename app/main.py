from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if not masks_to_buy:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {masks_to_buy} masks"
