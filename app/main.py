from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccination_errors = []
    for el in friends:
        if not el["wearing_a_mask"]:
            masks_to_buy += 1
        try:
            cafe.visit_cafe(el)
        except (NotVaccinatedError, OutdatedVaccineError):
            vaccination_errors.append(el)
        except NotWearingMaskError:
            pass

    if vaccination_errors:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
