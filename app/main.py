from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    num_mask = 0
    try:
        for count, friend in enumerate(friends):
            try:
                cafe.visit_cafe(friend)
            except (NotVaccinatedError,
                    OutdatedVaccineError):
                raise NotVaccinatedError
            except NotWearingMaskError:
                num_mask += 1
    except NotVaccinatedError:
        return "All friends should be vaccinated"
    else:
        if num_mask != 0:
            return f"Friends should buy {num_mask} masks"
        return f"Friends can go to {cafe.name}"
