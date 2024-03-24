from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str | None:
    mask_count: int = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_count += 1
    if mask_count == 0:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {mask_count} masks"
