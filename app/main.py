
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_in_musks = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            not_in_musks += 1

    if not_in_musks:
        return f"Friends should buy {not_in_musks} masks"

    return f"Friends can go to {cafe.name}"
