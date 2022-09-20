from app.errors import OutdatedVaccineError,\
    NotVaccinatedError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe):
    count_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_mask += 1
    if count_mask > 0:
        return f"Friends should buy {count_mask} masks"
    return f"Friends can go to {cafe.name}"
