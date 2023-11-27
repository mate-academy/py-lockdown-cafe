from app.cafe import Cafe
from typing import List, Union
from app.errors import (NotWearingMaskError, VaccineError)


def go_to_cafe(friends: List[dict], cafe: Cafe) -> Union[str, None]:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
