from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    result = f"Friends can go to {cafe.name}"
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            result = "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
            result = f"Friends should buy {masks_to_buy} masks"

    return result
