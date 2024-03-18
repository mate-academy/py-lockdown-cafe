from __future__ import annotations

from app.cafe import Cafe
from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    is_ok = True
    need_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            is_ok = False
            need_mask += 1
    if is_ok:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {need_mask} masks"
