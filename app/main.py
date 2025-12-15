from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    issues_found = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            issues_found += 1
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            issues_found += 1
            masks_to_buy += 1
    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"
    if issues_found == 0:
        return f"Friends can go to {cafe.name}"
