from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    without_masks_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            without_masks_count += 1

    if without_masks_count:
        return f"Friends should buy {without_masks_count} masks"

    return f"Friends can go to {cafe.name}"
