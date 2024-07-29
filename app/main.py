from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    not_vaccinated_or_outdated = False
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            not_vaccinated_or_outdated = True
            break
        except NotWearingMaskError:
            masks_to_buy += 1

    if not_vaccinated_or_outdated:
        return "All friends should be vaccinated"

    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    else:
        return f"Friends can go to {cafe.name}"
