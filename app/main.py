from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    counter_wearing_mask = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            counter_wearing_mask += 1
    if counter_wearing_mask:
        return f"Friends should buy {counter_wearing_mask} masks"
    return f"Friends can go to {cafe.name}"
