from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(cafe: Cafe, friends: list[dict]) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (
            VaccineError,
            NotWearingMaskError
        ) as e:
            if isinstance(e, VaccineError):
                return "All friends should be vaccinated"
            elif isinstance(e, NotWearingMaskError):
                masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
