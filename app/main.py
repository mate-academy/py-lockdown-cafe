from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_masks = 0
    for friend in friends:
        try:
            Cafe.visit_cafe(cafe, visitor=friend)
        except NotWearingMaskError:
            count_masks += 1
        except VaccineError:
            return "All friends should be vaccinated"
    if count_masks:
        return f"Friends should buy {count_masks} masks"

    return f"Friends can go to {cafe.name}"
