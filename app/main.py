from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError

def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except VaccineError:
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        masks_to_buy = sum(not friend.get("wearing_a_mask", False) for friend in friends)
        if masks_to_buy > 0:
            return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
