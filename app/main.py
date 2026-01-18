from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_count = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_count += 1
    if mask_count != 0:
        return f"Friends should buy {mask_count} masks"
    return f"Friends can go to {cafe.name}"
