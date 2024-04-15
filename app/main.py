from app.cafe import Cafe

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for mate in friends:
        if mate["wearing_a_mask"] is False:
            masks_to_buy += 1

    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except (OutdatedVaccineError, NotVaccinatedError):
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
