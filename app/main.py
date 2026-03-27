import datetime
from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
        for friend in friends:
            if "vaccine" not in friend:
                raise NotVaccinatedError("All friends should be vaccinated")
            if friend["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("All friends should be vaccinated")

        for friend in friends:
            cafe.visit_cafe(friend)

        return f"Friends can go to {cafe.name}"

    except (NotVaccinatedError, OutdatedVaccineError) as e:
        return str(e)

    except NotWearingMaskError:
        masks_to_buy = sum(
            1 for friend in friends if not friend.get("wearing_a_mask", False)
        )
        return f"Friends should buy {masks_to_buy} masks"
