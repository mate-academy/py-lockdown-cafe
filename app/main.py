from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_vaccinated = []
    not_wearing_mask = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            not_vaccinated.append(friend["name"])
        except NotWearingMaskError:
            not_wearing_mask += 1

    if not_vaccinated:
        return "All friends should be vaccinated"

    if not_wearing_mask > 0:
        return f"Friends should buy {not_wearing_mask} masks"

    return f"Friends can go to {cafe.name}"
