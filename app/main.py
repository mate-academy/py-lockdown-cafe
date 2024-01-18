from __future__ import annotations
from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


# ==== main ====
def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    no_mask = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                no_mask += 1
    except (OutdatedVaccineError, NotVaccinatedError):
        return "All friends should be vaccinated"

    if no_mask:
        return f"Friends should buy {no_mask} masks"
    else:
        return f"Friends can go to {cafe.name}"
