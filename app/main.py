from typing import Any
from app.cafe import Cafe
from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> Any:
    # cafe_name = Cafe(cafe)
    # print(cafe_name.name)
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy == 0:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {masks_to_buy} masks"
