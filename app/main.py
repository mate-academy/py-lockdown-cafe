from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vac_errors = []
    mask_errors = []
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vac_errors.append(None)
        except NotWearingMaskError:
            mask_errors.append(None)
    if vac_errors:
        return "All friends should be vaccinated"
    elif mask_errors:
        return f"Friends should buy {len(mask_errors)} masks"
    return f"Friends can go to {cafe.name}"
