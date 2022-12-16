from app.errors import NotWearingMaskError
from app.errors import VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_buy += 1
    if masks_buy > 0:
        return f"Friends should buy {masks_buy} masks"
    return f"Friends can go to {cafe.name}"
