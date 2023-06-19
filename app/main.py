from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_problems = 0
    mask_problems = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_problems += 1
        except NotWearingMaskError:
            mask_problems += 1

    if vaccine_problems != 0:
        return "All friends should be vaccinated"
    elif mask_problems != 0:
        return f"Friends should buy {mask_problems} masks"
    else:
        return f"Friends can go to {cafe.name}"
