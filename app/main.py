from __future__ import annotations

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_error_msg = []
    mask_error_msg = []
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as e:
            print(f"Vaccine error for {friend['name']}: {e}")
            vaccine_error_msg.append(e)
        except NotWearingMaskError as e:
            print(e)
            mask_error_msg.append(e)

    if not vaccine_error_msg and not mask_error_msg:
        return f"Friends can go to {cafe.name}"
    if vaccine_error_msg:
        return "All friends should be vaccinated"
    if not vaccine_error_msg and mask_error_msg:
        return f"Friends should buy {len(mask_error_msg)} masks"
