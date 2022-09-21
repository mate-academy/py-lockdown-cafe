from app.cafe import Cafe
from app.errors import NotVaccinatedError,\
    OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe):
    visitors_without_violations = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            if Cafe.visit_cafe(cafe, friend):
                visitors_without_violations += 1
        except (OutdatedVaccineError, NotVaccinatedError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if visitors_without_violations != len(friends):
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
