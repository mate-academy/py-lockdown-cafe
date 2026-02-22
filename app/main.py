from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str | None:
    masks_to_buy = 0
    can_go = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
        else:
            can_go += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    if can_go == len(friends):
        return f"Friends can go to {cafe.name}"
    return None
