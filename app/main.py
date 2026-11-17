from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)
from app.cafe import Cafe


def go_to_cafe(friends: list[dict[str, int | str]], cafe: Cafe) -> str:
    musks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            musks_to_buy += 1
        except (OutdatedVaccineError, NotVaccinatedError):
            return "All friends should be vaccinated"
    if musks_to_buy > 0:
        return f"Friends should buy {musks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
