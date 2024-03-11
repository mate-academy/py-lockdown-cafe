from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            continue
    try:
        [cafe.visit_cafe(friend) for friend in friends]
    except (NotVaccinatedError, OutdatedVaccineError):
        pass
    except NotWearingMaskError:
        masks_to_buy = \
            sum(1 for friend in friends if not friend["wearing_a_mask"])
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
