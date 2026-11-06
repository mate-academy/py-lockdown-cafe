from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError

from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    for index, friend in enumerate(friends):
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError) as e:
            return str(e)
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
