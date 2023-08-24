from __future__ import annotations
from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def get_amount_without_mask(friends: list) -> int:
    return len([friend for friend in friends if not friend["wearing_a_mask"]])


def go_to_cafe(friends: list, cafe: Cafe) -> str:

    for i, friend in enumerate(friends):
        try:
            cafe.visit_cafe(friend)
            if i == len(friends) - 1 and get_amount_without_mask(friends) != 0:
                return (f"Friends should buy "
                        f"{get_amount_without_mask(friends)} masks")

        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            if i == len(friends) - 1 and get_amount_without_mask(friends) != 0:
                return (f"Friends should buy "
                        f"{get_amount_without_mask(friends)} masks")

    return f"Friends can go to {cafe.name}"
