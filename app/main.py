from __future__ import annotations

from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    not_vaccinated_counter = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_vaccinated_counter += 1
        except NotWearingMaskError:
            masks_to_buy += 1

    if not_vaccinated_counter:
        return "All friends should be vaccinated"
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
