from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    no_problems = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return f"All friends should be vaccinated"
        except NotWearingMaskError:
            no_problems = False
            masks_to_buy += 1
    if no_problems:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {masks_to_buy} masks"

