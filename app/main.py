from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            not_masks += 1
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
    if not_masks:
        return f"Friends should buy {not_masks} masks"
    else:
        return f"Friends can go to {cafe.name}"
