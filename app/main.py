from cafe import Cafe
from errors import NotWearingMaskError, VaccineError


def go_to_cafe(
    friends: list[dict],
    cafe: Cafe
) -> str:
    masks_to_buy = 0

    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except VaccineError:
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        for friend in friends:
            if not friend.get("wearing_a_mask"):
                masks_to_buy += 1
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
