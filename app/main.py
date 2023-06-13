from app.cafe import Cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe):
    try:
        for friend in friends:
            cafe.visit_cafe(friend)
        return f"Friends can go to {cafe.name}"
    except (NotVaccinatedError, OutdatedVaccineError):
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        masks_to_buy = sum(1 for friend in friends if "wearing_a_mask" in friend and not friend["wearing_a_mask"])
        return f"Friends should buy {masks_to_buy} masks"



