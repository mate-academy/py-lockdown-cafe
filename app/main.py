from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> None:
    unvaccinated = 0
    no_mask = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError, OutdatedVaccineError:
            unvaccinated += 1
        except NotWearingMaskError:
            no_mask += 1

    if unvaccinated == 0 and no_mask > 0:
        masks_to_buy = no_mask
        return f"Friends should buy {masks_to_buy} masks"
    elif unvaccinated > 0:
        return "All friends should be vaccinated"
    return f"Friends can go to {cafe.name}"
