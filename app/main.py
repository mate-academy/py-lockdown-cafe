from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: dict, cafe: Cafe) -> str:
    masks_needed = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_needed += 1

    if masks_needed == 0:
        return f"Friends can go to {cafe.name}"
    return (
        "Friends should buy {} mask{}".
        format(masks_needed, "s" if masks_needed > 1 else "")
    )
