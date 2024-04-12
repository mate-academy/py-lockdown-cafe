from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    vaccine_errors = []
    mask_errors = []

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            vaccine_errors.append(f"{friend['name']} is not vaccinated.")
        except OutdatedVaccineError:
            vaccine_errors.append(f"{friend['name']}'s vaccine has expired.")
        except NotWearingMaskError:
            mask_errors.append(f"{friend['name']} is not wearing a mask")

    if vaccine_errors:
        return "All friends should be vaccinated"
    elif mask_errors:
        return f"Friends should buy {len(mask_errors)} masks"

    return f"Friends can go to {cafe.name}"
