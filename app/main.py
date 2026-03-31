from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    need_masks = 0
    not_vaccinated = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            not_vaccinated = True
        except NotWearingMaskError:
            need_masks += 1

    if not_vaccinated:
        return "All friends should be vaccinated"

    if need_masks > 0:
        return f"Friends should buy {need_masks} masks"

    return f"Friends can go to {cafe.name}"
