from app.errors import NotVaccinatedError,\
    OutdatedVaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError as error_info:
            return str(error_info)
        except OutdatedVaccineError as error_info:
            return str(error_info)
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
