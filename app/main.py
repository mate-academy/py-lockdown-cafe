from app.cafe import Cafe

from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    no_masks_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (OutdatedVaccineError, NotVaccinatedError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            no_masks_count += 1
    if no_masks_count > 0:
        return f"Friends should buy {no_masks_count} masks"
    return f"Friends can go to {cafe.name}"
