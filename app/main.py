from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            count_mask += 1
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            continue
    if count_mask == len(friends):
        return "Friends can go to KFC"
    return f"Friends should buy {len(friends) - count_mask} masks"
