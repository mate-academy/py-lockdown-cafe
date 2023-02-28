from app.cafe import Cafe
from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    can_go = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError:
            can_go += 1
            return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    elif can_go == 0:
        return f"Friends can go to {cafe.name}"
