from app.cafe import Cafe
from app.errors import VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    try:
        for friend in friends:
            cafe.visit_cafe({
                **friend,
                "wearing_a_mask": True,
            })
    except VaccineError:
        return "All friends should be vaccinated"

    masks_to_buy = sum(
        1 for friend in friends if not friend.get("wearing_a_mask", False)
    )

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
