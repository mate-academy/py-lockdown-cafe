from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_issues = False
    masks_needed = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            vaccine_issues = True
            break
        except NotWearingMaskError:
            masks_needed += 1

    if vaccine_issues:
        return "All friends should be vaccinated"
    elif masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"
    else:
        return f"Friends can go to {cafe.name}"
