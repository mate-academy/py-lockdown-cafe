from __future__ import annotations
from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


# ==== main ====
def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    no_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            no_mask += 1
        except (VaccineError):
            return "All friends should be vaccinated"

    if no_mask:
        return f"Friends should buy {no_mask} masks"
    return f"Friends can go to {cafe.name}"
