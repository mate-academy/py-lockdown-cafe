from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    masks_to_buy = 0
    vaccine_problem_found = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except NotWearingMaskError:
            masks_to_buy += 1

        except VaccineError:
            vaccine_problem_found = True
            break

    if vaccine_problem_found:
        return "All friends should be vaccinated"

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
