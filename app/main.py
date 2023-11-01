from app.cafe import Cafe
from app.errors import (
    NotWearingMaskError,
    VaccineError,
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    mask_errors = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as e:
            return str(e)
        except NotWearingMaskError:
            mask_errors += 1

    if mask_errors:
        return f"Friends should buy {mask_errors} masks"
    return f"Friends can go to {cafe.name}"
