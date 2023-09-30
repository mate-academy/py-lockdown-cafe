from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    without_mask_count = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            without_mask_count += 1

    if without_mask_count != 0:
        return f"Friends should buy {without_mask_count} masks"

    return f"Friends can go to {cafe.name}"
