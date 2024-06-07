from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    is_access = True
    is_vaccinated = True
    masks_not_worn = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_not_worn += 1
            is_access = False
        except (NotVaccinatedError, OutdatedVaccineError):
            is_access = False
            is_vaccinated = False
    if is_access:
        return f"Friends can go to {cafe.name}"
    if masks_not_worn:
        return f"Friends should buy {masks_not_worn} masks"
    if not is_vaccinated:
        return "All friends should be vaccinated"
