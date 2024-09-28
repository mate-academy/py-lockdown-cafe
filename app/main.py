from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: object):
    mask_needed = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_needed += 1
    if mask_needed > 0:
        return f"Friends should buy {mask_needed} masks"
    return f"Friends can go to {cafe.name}"
