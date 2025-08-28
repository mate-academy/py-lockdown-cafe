from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count = 0
    masks_to_buy = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            count += 1
        except NotWearingMaskError:
            masks_to_buy += 1
    if count:
        return "All friends should be vaccinated"
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
