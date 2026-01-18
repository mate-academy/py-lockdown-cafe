import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    try:
        for friend in friends:
            cafe.visit_cafe(friend)
        return f"Friends can go to {cafe.name}"
    except (NotVaccinatedError, OutdatedVaccineError):
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        masks_to_buy = sum(
            not friend.get("wearing_a_mask", False) for friend in friends
        )
        if all("vaccine" in friend and friend["vaccine"]["expiration_date"]
               > datetime.date.today() for friend in friends):
            return f"Friends should buy {masks_to_buy} masks"
        else:
            return "All friends should be vaccinated"
