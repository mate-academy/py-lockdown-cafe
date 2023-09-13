from __future__ import annotations

from app.errors import VaccineError, NotWearingMaskError

from app.cafe import Cafe


def get_amount_without_mask(friends: list) -> int:
    return len([friend for friend in friends if not friend["wearing_a_mask"]])


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_without_mask = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_without_mask += 1

    if count_without_mask > 0:
        return f"Friends should buy {count_without_mask} masks"
    else:
        return f"Friends can go to {cafe.name}"
