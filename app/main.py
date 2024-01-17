import datetime

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError

day_today = datetime.date.today()


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    not_wearing_mask_error = None
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as v:
            return str(v)

        except NotWearingMaskError as n:

            masks_to_buy += 1
            not_wearing_mask_error = n

    if not_wearing_mask_error:
        return str(not_wearing_mask_error) + f"{masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
