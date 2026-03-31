from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_count = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)

        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            masks_count += 1

    if masks_count:
        return f"Friends should buy {masks_count} masks"

    return f"Friends can go to {cafe.name}"
