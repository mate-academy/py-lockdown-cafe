from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccinated_friends = 0
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            vaccinated_friends += 1
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
