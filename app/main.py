from __future__ import annotations

from app.errors import NotWearingMaskError,\
    OutdatedVaccineError, NotVaccinatedError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for one_visitor in friends:
        try:
            cafe.visit_cafe(one_visitor)

        except NotWearingMaskError:
            masks_to_buy += 1

        except (OutdatedVaccineError, NotVaccinatedError):
            return "All friends should be vaccinated"

    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
