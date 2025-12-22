from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    has_no_errors = True
    masks_to_buy = 0
    vaccine_problem = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_problem = True
            has_no_errors = False
        except NotWearingMaskError:
            masks_to_buy += 1
            has_no_errors = False

    if vaccine_problem:
        return "All friends should be vaccinated"

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    if has_no_errors:
        return f"Friends can go to {cafe.name}"
