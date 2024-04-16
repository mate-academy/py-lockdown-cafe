from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError as e:
            print(e)
            return "All friends should be vaccinated"
        except NotWearingMaskError as e:
            print(e)
            masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
