import datetime

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError

day_today = datetime.date.today()


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    vaccine_error_encountered = False
    not_wearing_mask_error = None
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as v:
            vaccine_error_encountered = True
            return str(v)
        except NotWearingMaskError as n:
            if not vaccine_error_encountered:
                masks_to_buy += 1
                not_wearing_mask_error = n

    if vaccine_error_encountered:
        return str(vaccine_error_encountered)
    elif not_wearing_mask_error:
        return (str(not_wearing_mask_error) + 
                f"{masks_to_buy} masks")
    else:
        return f"Friends can go to {cafe.name}"
