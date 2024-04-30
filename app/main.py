from copy import deepcopy

from .cafe import Cafe
from .errors import NotWearingMaskError, VaccineError


def masks_to_buy(friends: list[dict]) -> int:
    return (
        len(
            [friend for friend in friends if friend["wearing_a_mask"] is False]
        )
    )


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    try:
        copy_friends = deepcopy(friends)
        for friend in copy_friends:
            friend["wearing_a_mask"] = True
            cafe.visit_cafe(friend)
    except VaccineError:
        return "All friends should be vaccinated"
    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except NotWearingMaskError:
        return f"Friends should buy {masks_to_buy(friends)} masks"
    else:
        return f"Friends can go to {cafe.name}"
