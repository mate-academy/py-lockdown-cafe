from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    ready_to_go = 0
    masks_to_buy = 0
    vaccine_problems = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            ready_to_go += 1
        except VaccineError:
            vaccine_problems += 1
        except NotWearingMaskError:
            masks_to_buy += 1

    if ready_to_go == len(friends):
        return f"Friends can go to {cafe.name}"
    if vaccine_problems > 0:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
