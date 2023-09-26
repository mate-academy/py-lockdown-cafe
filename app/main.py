from __future__ import annotations
from app.cafe import Cafe
from app.errors import NotWearingMaskError
from app.errors import VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    need_mask = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            need_mask += 1

    if need_mask == 0:
        return f"Friends can go to {cafe.name}"

    return f"Friends should buy {need_mask} masks"
