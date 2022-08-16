from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
    VaccineError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe):
    check_ok = True
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            check_ok = False
        except VaccineError:
            check_ok = False
        except NotWearingMaskError:
            # check_ok = False
            masks_to_buy += 1
    if not check_ok:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
