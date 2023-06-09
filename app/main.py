from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError
                        )


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy = sum(
                1 for friend in friends if not friend["wearing_a_mask"]
            )

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
