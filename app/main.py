from app.cafe import Cafe
from app.errors import NotWearingMaskError,\
    NotVaccinatedError, OutdatedVaccineError


def go_to_cafe(friends: list, cafe: Cafe):
    count_buy_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_buy_masks += 1
    if count_buy_masks > 0:
        return f"Friends should buy {count_buy_masks} masks"
    return f"Friends can go to {cafe.name}"
