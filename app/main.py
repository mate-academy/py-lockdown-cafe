from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    result = []
    masks_needed = 0
    for friend in friends:
        try:
            result.append(cafe.visit_cafe(friend))
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_needed += 1
    if len(result) == len(friends) and masks_needed == 0:
        return f"Friends can go to {cafe.name}"
    elif masks_needed != 0:
        return f"Friends should buy {masks_needed} masks"
