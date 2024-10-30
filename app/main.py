from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError, OutdatedVaccineError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    all_vaccinated = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            all_vaccinated = False
            break
        except NotWearingMaskError:
            masks_to_buy += 1
    if not all_vaccinated:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
