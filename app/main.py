from app.errors import (
    VaccineError, NotWearingMaskError
)

from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    problems_with_vaccination_count = 0
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            problems_with_vaccination_count += 1
        except NotWearingMaskError:
            masks_to_buy += 1

    if problems_with_vaccination_count:
        return "All friends should be vaccinated"

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
