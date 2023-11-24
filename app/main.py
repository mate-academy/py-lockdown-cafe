import datetime

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError

day_today = datetime.date.today()


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    vaccine_error = None
    mask_errors = []

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as v:
            vaccine_error = v
        except NotWearingMaskError as n:
            mask_errors.append(n)

    if vaccine_error:
        return str(vaccine_error)

    if mask_errors:
return (f"NotWearingMaskError: {mask_errors[0]}. "
        f"Friends should buy {len(mask_errors)} masks.")

    return f"Friends can go to {cafe.name}"
