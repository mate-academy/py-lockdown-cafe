from app.cafe import Cafe
# from app.errors import * bad practice or something?
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    without_mask = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            without_mask += 1
    if without_mask > 0:
        return f"Friends should buy {without_mask} masks"
    return f"Friends can go to {cafe.name}"
