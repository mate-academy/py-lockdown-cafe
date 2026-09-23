from __future__ import annotations
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError
from app.errors import NotVaccinatedError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    has_exceptions = False
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1
        except (OutdatedVaccineError, NotVaccinatedError):
            has_exceptions = True

    if has_exceptions:
        return "All friends should be vaccinated"

    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
