import datetime

from .cafe import Cafe
from .errors import (VaccineError,
                     NotWearingMaskError,
                     OutdatedVaccineError,
                     NotVaccinatedError)


def go_to_cafe(friends: list, cafe: Cafe) -> (None, str):
    masks_to_buy = sum(1 for j in friends if not j["wearing_a_mask"])
    today_date = datetime.date.today()

    for friend in friends:
        if "vaccine" not in friend:
            try:
                cafe.visit_cafe(friend)

            except NotVaccinatedError:
                return "All friends should be vaccinated"

        expiration_date = friend["vaccine"]["expiration_date"]
        if expiration_date < today_date:
            try:
                cafe.visit_cafe(friend)

            except OutdatedVaccineError:
                return "All friends should be vaccinated"

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except VaccineError as e:
            return e

        except NotWearingMaskError:
            return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
