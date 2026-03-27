from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    vac_errors = 0
    mask_errors = 0
    for friend in friends:
        try:
            print(cafe.visit_cafe(friend))
        except VaccineError as error:
            vac_errors += 1
            print(error)
        except NotWearingMaskError as error:
            mask_errors += 1
            print(error)
    if vac_errors:
        return "All friends should be vaccinated"
    if mask_errors:
        return f"Friends should buy {mask_errors} masks"
    return f"Friends can go to {cafe.name}"
