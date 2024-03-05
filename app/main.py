from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count = 0
    for person in friends:
        try:
            Cafe.visit_cafe(cafe, person)
        except (NotVaccinatedError, OutdatedVaccineError):
            return ("All friends should be vaccinated")
        except NotWearingMaskError:
            count += 1
    if count > 0:
        return (f"Friends should buy {count} masks")
    else:
        return (f"Friends can go to {cafe.name}")
