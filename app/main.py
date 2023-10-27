from app.cafe import Cafe
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_to_buy += 1
    if mask_to_buy:
        return f"Friends should buy {mask_to_buy} masks"
    return f"Friends can go to {cafe.name}"
