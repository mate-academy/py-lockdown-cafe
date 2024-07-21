from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_check = True
    mask_counter = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            vaccine_check = False
        except NotWearingMaskError:
            mask_counter += 1
    if not vaccine_check:
        return "All friends should be vaccinated"
    if mask_counter > 0:
        return f"Friends should buy {mask_counter} masks"
    return f"Friends can go to {cafe.name}"
