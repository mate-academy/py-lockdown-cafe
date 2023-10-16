from typing import Any
from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> Any:
    for one_friend in friends:
        try:
            cafe.visit_cafe(one_friend)
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            return f"Friends should buy {len(friends)} masks"
    return f"Friends can go to {cafe.name}"
