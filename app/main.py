from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    is_vaccine = True
    not_mask = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            is_vaccine = False
        except NotWearingMaskError:
            not_mask += 1
    if not is_vaccine:
        return "All friends should be vaccinated"
    if not_mask:
        return f"Friends should buy {not_mask} masks"
    return f"Friends can go to {cafe.name}"
