from typing import Type

from .cafe import Cafe
from .errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Type[Cafe]) -> str:
    mask_to_buy = False

    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_to_buy += 1

    if mask_to_buy is not False:
        return f"Friends should buy {mask_to_buy} masks"

    return f"Friends can go to {cafe.name}"
