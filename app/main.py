from app.cafe import Cafe
from app.errors import (VaccineError,
                        NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_req_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_req_masks += 1

    if count_req_masks:
        return f"Friends should buy {count_req_masks} masks"
    return f"Friends can go to {cafe.name}"
