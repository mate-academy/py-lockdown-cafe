from errors import VaccineError, NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
from  cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks += 1
            continue
    if masks > 0:
        return f"Friends should buy {masks} masks"
    return f"Friends can go to {cafe.name}"