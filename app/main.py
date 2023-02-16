from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_friends = 0
    count_masks = 0
    for friend in friends:
        try:
            Cafe.visit_cafe(cafe, visitor=friend)
            count_friends += 1
        except NotWearingMaskError:
            count_masks += 1
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
        except NotVaccinatedError:
            return "All friends should be vaccinated"
    if count_masks != 0:
        return f"Friends should buy {count_masks} masks"
    if count_friends == len(friends):
        return f"Friends can go to {cafe.name}"
