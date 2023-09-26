from app.cafe import Cafe
from app.errors import (
                        NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError
                        )


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = sum(1 for friend in friends if not friend.get("wearing_a_mask"))

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
