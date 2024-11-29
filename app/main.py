from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_mask = 0
    all_vaccinated = True

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            all_vaccinated = False
        except OutdatedVaccineError:
            all_vaccinated = False
        except NotWearingMaskError:
            count_mask += 1

    if not all_vaccinated:
        return "All friends should be vaccinated"

    if count_mask:
        return f"Friends should buy {count_mask} masks"

    return f"Friends can go to {cafe.name}"
