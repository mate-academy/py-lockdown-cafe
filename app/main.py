from app.cafe import Cafe
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe):
    masks_to_buy = 0
    count_accept_friends = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            count_accept_friends += 1
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if len(friends) == count_accept_friends:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {masks_to_buy} masks"
