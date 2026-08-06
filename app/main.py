from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)

def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    missing_vaccines = 0
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            missing_vaccines += 1
        except NotWearingMaskError:
            masks_to_buy += 1

    if missing_vaccines > 0:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
