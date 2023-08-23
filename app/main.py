from app.cafe import Cafe
from app.errors import NotWearingMaskError
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for i in friends:
        try:
            cafe.visit_cafe(i)
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
