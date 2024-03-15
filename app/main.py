from app.cafe import Cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_count = 0
    for friend in friends:
        try:
            Cafe.visit_cafe(cafe, friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_count += 1
    if masks_count > 0:
        return f"Friends should buy {masks_count} masks"
    return f"Friends can go to {cafe.name}"
