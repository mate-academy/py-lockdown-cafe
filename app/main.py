from app.errors import VaccineError
from app.errors import NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: dict, cafe: Cafe) -> str:
    vaccine_problem = False
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError:
            vaccine_problem = True

    if vaccine_problem:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return "Friends can go to KFC"
