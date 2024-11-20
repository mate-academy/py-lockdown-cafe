from app.cafe import Cafe
from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_issues = 0

    for friend in friends:
        try:
            Cafe.visit_cafe(cafe, friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_issues += 1

    if mask_issues > 0:
        return f"Friends should buy {mask_issues} masks"

    return f"Friends can go to {cafe.name}"
