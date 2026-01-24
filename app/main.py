from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict]) -> str:
    cafe = Cafe()

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"

    masks_to_buy = sum(1 for friend in friends if not friend.get("wearing_a_mask", False))
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return "Friends can go to the cafe"
