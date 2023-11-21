
from app.cafe import Cafe

from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    errors = []
    masks_to_buy = 0

    for visitor in friends:

        try:
            cafe.visit_cafe(visitor)
        except VaccineError as e:
            errors.append(e)
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy >= 1:
        return f"Friends should buy {masks_to_buy} masks"

    if not errors:
        return f"Friends can go to {cafe.name}"
