from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError
import datetime


def go_to_cafe(friends: list, cafe: Cafe) -> None | str:
    date_today = datetime.date.today()

    try:
        for friend in friends:
            if "vaccine" not in friend:
                raise NotVaccinatedError
            if date_today > friend["vaccine"]["expiration_date"]:
                raise OutdatedVaccineError
    except VaccineError:
        return "All friends should be vaccinated"

    mask_counter = sum(1 for friend in friends
                       if not friend.get("wearing_a_mask", False))

    if mask_counter > 0:
        return f"Friends should buy {mask_counter} masks"

    return f"Friends can go to {cafe.name}"