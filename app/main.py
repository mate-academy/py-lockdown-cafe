from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_needed = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError as e:
            return e.__str__()
        except OutdatedVaccineError as e:
            return e.__str__()
        except NotWearingMaskError:
            masks_needed += 1

    if masks_needed > 0:
        return NotWearingMaskError(masks_needed).__str__()
    return f"Friends can go to {cafe.name}"
