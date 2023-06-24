from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError
from app.errors import NotVaccinatedError
from app.cafe import Cafe
from typing import List, Dict


def go_to_cafe(friends: List[Dict[str, any]], cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
