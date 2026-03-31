from __future__ import annotations

from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(visitor=friend)
        except NotWearingMaskError:
            friends_without_mask += 1
        except VaccineError:
            return "All friends should be vaccinated"

    return (f"Friends can go to {cafe.name}" if not friends_without_mask
            else f"Friends should buy {friends_without_mask} masks")
