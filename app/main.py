from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    unvaccinated = False
    masks_to_buy = 0

    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                masks_to_buy += 1
    except NotVaccinatedError:
        unvaccinated = True
    except OutdatedVaccineError:
        unvaccinated = True

    if unvaccinated:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
