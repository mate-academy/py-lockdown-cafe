from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except VaccineError:
                return "All friends should be vaccinated"
            except NotWearingMaskError:
                masks_to_buy += 1
                pass
        if masks_to_buy:
            raise NotWearingMaskError
    except NotWearingMaskError:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
