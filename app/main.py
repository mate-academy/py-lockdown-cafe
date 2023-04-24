from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    masks_to_buy = 0
    all_allowed = True
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            masks_to_buy += 1
            all_allowed = False

    if all_allowed:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {masks_to_buy} masks"
