from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_problems = 0
    mask_problems = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as ve:
            print(ve)
            vaccine_problems += 1
        except NotWearingMaskError as wme:
            print(wme)
            mask_problems += 1

    if vaccine_problems != 0:
        return "All friends should be vaccinated"
    elif vaccine_problems == 0 and mask_problems != 0:
        return f"Friends should buy {mask_problems} masks"
    return f"Friends can go to {cafe.name}"
