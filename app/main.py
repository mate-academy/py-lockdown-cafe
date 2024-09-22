from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError) as vaccine_error:
            return str(vaccine_error)
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy:
        return str(NotWearingMaskError(masks_to_buy))

    return f"Friends can go to {cafe.name}"
