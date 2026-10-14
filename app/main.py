from app.cafe import Cafe
from app.errors import VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"

    friends_without_masks = [
        friend for friend in friends
        if not friend.get("wearing_a_mask", False)
    ]

    if friends_without_masks:
        masks_to_buy = len(friends_without_masks)
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
