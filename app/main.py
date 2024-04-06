from __future__ import annotations

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    someone_not_vaccinated = False
    someone_not_masked = False
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            someone_not_vaccinated = True
        except NotWearingMaskError:
            someone_not_masked = True
            masks_to_buy = sum(not friend.get("wearing_a_mask", False)
                               for friend in friends)

    if someone_not_vaccinated:
        return "All friends should be vaccinated"
    elif someone_not_masked:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
