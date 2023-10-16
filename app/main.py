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
        except NotVaccinatedError or OutdatedVaccineError:
            raise
        except NotWearingMaskError:
            raise
    return f"Friends can go to {cafe.name}"
