import datetime

from app.errors import (
    VaccineError,
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            if not friend.get("vaccine"):
                raise NotVaccinatedError
            if (friend.get("vaccine").get("expiration_date")
                    < datetime.date.today()):
                raise OutdatedVaccineError
            if not friend.get("wearing_a_mask"):
                masks_to_buy += 1
        except VaccineError:
            return "All friends should be vaccinated"

    try:
        if masks_to_buy > 0:
            raise NotWearingMaskError
    except NotWearingMaskError:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
