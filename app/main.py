from app.cafe import Cafe
from app.errors import \
    NotVaccinatedError, \
    OutdatedVaccineError,\
    NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    is_vaccinated = True

    for idx, friend in enumerate(friends):
        try:
            cafe.visit_cafe(friend)

        except NotWearingMaskError:
            masks_to_buy += 1

        except (KeyError, NotVaccinatedError, OutdatedVaccineError):
            is_vaccinated = False
            break

    if not is_vaccinated:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
