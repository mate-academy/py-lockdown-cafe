from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = len(friends)
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            masks_to_buy -= 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            pass
    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
