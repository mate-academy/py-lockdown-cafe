from app.cafe import Cafe
from app.errors import (
    NotWearingMaskError,
    VaccineError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_needed = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as e:
            return str(e)
        except NotWearingMaskError:
            masks_needed += 1

    if masks_needed:
        return str(NotWearingMaskError(masks_needed))
    return f"Friends can go to {cafe.name}"
