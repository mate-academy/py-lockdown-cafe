from typing import Any


from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list[dict[str, Any]], cafe: Cafe) -> str:
    unvaccinated_friend = False
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            unvaccinated_friend = True
        except NotWearingMaskError:
            masks_to_buy += 1
    if unvaccinated_friend:
        return "All friends should be vaccinated"
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
