from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    if not friends:
        return "No friends to check."

    vaccinated = True
    no_mask_count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            vaccinated = False
        except OutdatedVaccineError:
            vaccinated = False
        except NotWearingMaskError:
            no_mask_count += 1

    if not vaccinated:
        return "All friends should be vaccinated"

    if no_mask_count > 0:
        return f"Friends should buy {no_mask_count} masks"

    return f"Friends can go to {cafe.name}"
