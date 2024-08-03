from datetime import date
from app.cafe import Cafe
from app.errors import (VaccineError,
                        NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for friend in friends:
            vaccine = friend.get("vaccine")
            if not vaccine:
                raise NotVaccinatedError(
                    f"{friend['name']} is not vaccinated."
                )
            if vaccine["expiration_date"] < date.today():
                raise OutdatedVaccineError(
                    f"{friend['name']}'s vaccine is expired."
                )
            if not friend.get("wearing_a_mask", True):
                masks_to_buy += 1

        if masks_to_buy > 0:
            return f"Friends should buy {masks_to_buy} masks"

        return f"Friends can go to {cafe.name}"

    except NotVaccinatedError:
        return "All friends should be vaccinated"
    except OutdatedVaccineError:
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        return f"Friends should buy {masks_to_buy} masks"
    except VaccineError:
        return "All friends should be vaccinated"
