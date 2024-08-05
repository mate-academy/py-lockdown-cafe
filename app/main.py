from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
            continue
    return (
        f"Friends can go to {cafe.name}" if masks_to_buy == 0
        else f"Friends should buy {masks_to_buy} masks"
    )
