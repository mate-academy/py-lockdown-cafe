from app.cafe import Cafe
from app.errors import NotVaccinatedError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    for visitor in friends:
        try:
            if not cafe.visit_cafe(visitor):
                pass
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        try:
            if not visitor["wearing_a_mask"]:
                masks_to_buy += 1
        except NotWearingMaskError:
            return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
