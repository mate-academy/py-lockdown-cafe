from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    not_vaccinated = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_vaccinated = True
        except NotWearingMaskError:
            masks_to_buy += 1

    if not_vaccinated:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
