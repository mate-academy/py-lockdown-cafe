from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    is_vaccine = ""
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            is_vaccine = "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if is_vaccine != "":
        return is_vaccine
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
