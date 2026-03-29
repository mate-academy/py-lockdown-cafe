from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    vaccine_error_count = 0
    not_wearing_mask_count = 0

    for friend in friends:

        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_error_count += 1
        except NotWearingMaskError:
            not_wearing_mask_count += 1

    if vaccine_error_count:
        return "All friends should be vaccinated"
    if not_wearing_mask_count:
        return f"Friends should buy {not_wearing_mask_count} masks"

    return f"Friends can go to {cafe.name}"
