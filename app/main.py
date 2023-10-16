from typing import Any
from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> Any:
    mask_to_buy = 0
    for one_friend in friends:
        try:
            cafe.visit_cafe(one_friend)
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_to_buy += 1
    if mask_to_buy > 0:
        return f"Friends should buy {mask_to_buy} masks"
    return f"Friends can go to {cafe.name}"
