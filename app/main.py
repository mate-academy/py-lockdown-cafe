from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    ok_counter = 0
    masks_to_buy = 0
    for element in friends:
        try:
            cafe.visit_cafe(element)
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
        else:
            ok_counter += 1
    if ok_counter == len(friends):
        return f"Friends can go to {cafe.name}"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
