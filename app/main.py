from __future__ import annotations
from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    mask_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            mask_to_buy += 1
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
    if mask_to_buy:
        return f"Friends should buy {mask_to_buy} masks"
    return f"Friends can go to {cafe.name}"
