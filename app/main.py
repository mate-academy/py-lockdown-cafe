from app.cafe import Cafe
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    maskless_count = 0

    for index, friend in enumerate(friends):
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            maskless_count += 1

    if maskless_count > 0:
        return f"Friends should buy {maskless_count} masks"

    return f"Friends can go to {cafe.name}"
