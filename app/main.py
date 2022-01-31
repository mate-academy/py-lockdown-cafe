from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe):
    masks_to_buy = 0
    is_vaccine = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            is_vaccine = False
        except NotWearingMaskError:
            masks_to_buy += 1
    if not is_vaccine:
        return 'All friends should be vaccinated'
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
