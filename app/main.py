from .errors import VaccineError, NotWearingMaskError
from .cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    unvaccinated = False
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            unvaccinated = True
        except NotWearingMaskError:
            masks_to_buy += 1

    if unvaccinated:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
