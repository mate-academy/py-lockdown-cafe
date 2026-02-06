from cafe import Cafe
from errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    mask_problems = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_problems += 1

    if mask_problems:
        return f"Friends should buy {mask_problems} masks"

    return f"Friends can go to {cafe.name}"
