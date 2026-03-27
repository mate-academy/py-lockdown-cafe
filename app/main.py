from typing import List

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)

from app.cafe import Cafe


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    not_vaccinated = []
    outdated_vaccine = []
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            not_vaccinated.append(friend)
        except OutdatedVaccineError:
            outdated_vaccine.append(friend)
        except NotWearingMaskError:
            masks_to_buy += 1

    if not_vaccinated:
        return "All friends should be vaccinated"
    elif outdated_vaccine:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
