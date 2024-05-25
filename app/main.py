from app.errors import NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    wearing_masks = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
            wearing_masks = False
    if not wearing_masks:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
