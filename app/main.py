from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccinated = True
    mask_not_wear_count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccinated = False
        except NotWearingMaskError:
            mask_not_wear_count += 1

    if not vaccinated:
        return "All friends should be vaccinated"
    elif mask_not_wear_count > 0:
        return f"Friends should buy {mask_not_wear_count} masks"
    else:
        return f"Friends can go to {cafe.name}"
