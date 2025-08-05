from app.cafe import Cafe
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    missing_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            missing_masks += 1
    if missing_masks == 0:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {missing_masks} masks"
