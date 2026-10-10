from .errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)
from .cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str | None:
    vaccine_false = False
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            vaccine_false = True
        except NotWearingMaskError:
            masks_to_buy += 1

    if vaccine_false:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
