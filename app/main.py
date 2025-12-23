from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccine_problem = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError:
            vaccine_problem += 1
    if masks_to_buy == 0 and vaccine_problem == 0:
        return f"Friends can go to {cafe.name}"
    if vaccine_problem > 0:
        return "All friends should be vaccinated"
    if vaccine_problem == 0 and masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
