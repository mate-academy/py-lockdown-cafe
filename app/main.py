from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_for_friends = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_for_friends += 1
    if masks_for_friends > 0:
        return f"Friends should buy {masks_for_friends} masks"
    return f"Friends can go to {cafe.name}"
