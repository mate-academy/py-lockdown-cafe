from app.cafe import Cafe
from app.errors import (VaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    vac_issue = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vac_issue += 1
        except NotWearingMaskError:
            masks_to_buy += 1
    if vac_issue:
        return "All friends should be vaccinated"
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
