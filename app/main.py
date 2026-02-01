from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str | None:
    errors = []
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            errors.append("VaccineError")
        except NotWearingMaskError:
            errors.append("NotWearingMaskError")

    if "VaccineError" in errors:
        return "All friends should be vaccinated"
    if "NotWearingMaskError" in errors:
        masks_to_buy = len(
            [friend for friend in friends if not friend["wearing_a_mask"]]
        )
        return f"Friends should buy {masks_to_buy} masks"
    if not errors:
        return f"Friends can go to {cafe.name}"
