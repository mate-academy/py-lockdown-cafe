from app.cafe import Cafe
from app.errors import (
    NotWearingMaskError,
    VaccineError,
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    mask_errors = []
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as e:
            return str(e)
        except NotWearingMaskError as e:
            mask_errors.append(e)

    if mask_errors:
        return f"{str(mask_errors[0])[:-6]} {len(mask_errors)} masks"

    return f"Friends can go to {cafe.name}"
