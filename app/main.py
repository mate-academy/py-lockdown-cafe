from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_required = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_required = masks_required + 1
    if masks_required != 0:
        return f"Friends should buy {masks_required} masks"
    return f"Friends can go to {cafe.name}"
