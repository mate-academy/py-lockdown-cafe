from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy = len([
                f for f in friends
                if not f.get("wearing_a_mask")
            ])
            return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
