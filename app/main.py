from typing import List, Dict, Any

from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(
    friends: List[Dict[str, Any]],
    cafe: Cafe,
) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            continue

    without_mask = 0

    for friend in friends:
        if not friend.get("wearing_a_mask"):
            without_mask += 1

    if without_mask > 0:
        return f"Friends should buy {without_mask} masks"

    return f"Friends can go to {cafe.name}"
