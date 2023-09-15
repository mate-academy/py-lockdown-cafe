from app.errors import (OutdatedVaccineError, NotWearingMaskError,
                        NotVaccinatedError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            if friend["wearing_a_mask"] is False:
                masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
