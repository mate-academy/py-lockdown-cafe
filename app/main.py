from typing import Union

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> Union[
    VaccineError,
    NotWearingMaskError,
    str
]:
    masks_to_buy: int = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
