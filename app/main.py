from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(
        friends: list[dict],
        cafe: Cafe
) -> str:
    someone_has_vaccine_problem = False
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            someone_has_vaccine_problem = True
        except NotWearingMaskError:
            masks_to_buy += 1

    if someone_has_vaccine_problem:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
