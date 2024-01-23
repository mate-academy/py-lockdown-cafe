from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    check_mask = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            check_mask += 1
    if check_mask > 0:
        return f"Friends should buy {check_mask} masks"
    return f"Friends can go to {cafe.name}"
