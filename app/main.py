from app.errors import VaccineError, NotWearingMaskError, VaccineMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_errors = 0
    mask_errors = 0

    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except (VaccineMaskError):
            mask_errors += 1
            vaccine_errors += 1
        except (VaccineError):
            vaccine_errors += 1
        except (NotWearingMaskError):
            mask_errors += 1

    if vaccine_errors == 0 and mask_errors == 0:
        return f"Friends can go to {cafe.name}"
    if vaccine_errors > 0:
        return "All friends should be vaccinated"
    if mask_errors > 0:
        return f"Friends should buy {mask_errors} masks"
