from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    any_issues = False
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            any_issues = True
            masks_to_buy += 1
    if not any_issues:
        return f"Friends can go to {cafe.name}"

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
