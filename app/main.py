from app.cafe import Cafe
from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_friends = 0
    dont_vaccinated = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (OutdatedVaccineError, NotVaccinatedError):
            dont_vaccinated += 1
        except NotWearingMaskError:
            count_friends += 1

    if dont_vaccinated > 0:
        return "All friends should be vaccinated"
    if count_friends > 0:
        return f"Friends should buy {count_friends} masks"

    return f"Friends can go to {cafe.name}"
