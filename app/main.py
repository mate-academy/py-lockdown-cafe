from app.cafe import Cafe
from app.errors import NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    required_masks = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except (OutdatedVaccineError, NotVaccinatedError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            required_masks += 1

    if required_masks != 0:
        return f"Friends should buy {required_masks} masks"

    return f"Friends can go to {cafe.name}"
