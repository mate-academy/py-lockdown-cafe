from typing import List
from app.errors import NotVaccinatedError, OutdatedVaccineError
from app.cafe import Cafe
import datetime


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    for friend in friends:
        try:
            if "vaccine" not in friend:
                raise NotVaccinatedError
            if friend["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"

    masks_to_buy = sum(
        1 for f in friends if not f.get("wearing_a_mask", False)
    )
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
