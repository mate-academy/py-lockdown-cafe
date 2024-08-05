from app.cafe import Cafe

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    if not friends:
        return "No friends to check."

    no_mask_count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            no_mask_count += 1

    if no_mask_count:
        return f"Friends should buy {no_mask_count} masks"

    return f"Friends can go to {cafe.name}"
