from typing import List, Dict
from .cafe import Cafe
from .errors import (NotVaccinatedError,
                     OutdatedVaccineError,
                     NotWearingMaskError)


def go_to_cafe(friends: List[Dict[str, any]], cafe: Cafe) -> str:
    masks_needed = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            # Handles both NotVaccinatedError and OutdatedVaccineError
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_needed += 1

    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"
    return f"Friends can go to {cafe.name}"
