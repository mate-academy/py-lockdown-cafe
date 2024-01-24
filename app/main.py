from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_needs_count = 0
    for friend in friends:
        try:
            Cafe.visit_cafe(cafe, visitor=friend)

        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            mask_needs_count += 1

    if mask_needs_count:
        return f"Friends should buy {mask_needs_count} masks"
    return f"Friends can go to {cafe.name}"
