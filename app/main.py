from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccination_issues = False
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccination_issues = True
        except NotWearingMaskError:
            masks_to_buy += 1
    if vaccination_issues:
        return "All friends should be vaccinated"
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
