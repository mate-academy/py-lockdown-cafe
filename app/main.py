import datetime

from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotVaccinatedError,
    OutdatedVaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
        for friend in friends:
            if "vaccine" not in friend:
                raise NotVaccinatedError("No vaccine record.")

            expiration_date = friend["vaccine"]["expiration_date"]
            if expiration_date < datetime.date.today():
                raise OutdatedVaccineError("Vaccine expired.")
    except VaccineError:
        return "All friends should be vaccinated"

    masks_to_buy = 0
    for friend in friends:
        if not friend.get("wearing_a_mask"):
            masks_to_buy += 1

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
