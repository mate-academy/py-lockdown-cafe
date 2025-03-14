from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from datetime import datetime


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    all_vaccinated = True

    for friend in friends:
        try:
            if "vaccine" not in friend:
                raise NotVaccinatedError("Visitor is not vaccinated")

            expiration_date = friend["vaccine"]["expiration_date"]

            if expiration_date < datetime.today().date():
                raise OutdatedVaccineError("The vaccine is expired,"
                                           " entry denied.")

            if not friend["wearing_a_mask"]:
                masks_to_buy += 1

        except NotVaccinatedError:
            all_vaccinated = False
            return "All friends should be vaccinated"
        except OutdatedVaccineError:
            all_vaccinated = False
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if not all_vaccinated:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
