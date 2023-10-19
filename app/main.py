import datetime

from app.cafe import Cafe
from app.errors import OutdatedVaccineError, VaccineError
from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    today_date = datetime.date.today()

    try:
        for friend in friends:

            if "vaccine" not in friend:
                raise NotVaccinatedError("All friends should be vaccinated")

            expiration_date = friend.get("vaccine")["expiration_date"]

            if expiration_date < today_date:
                raise OutdatedVaccineError("All friends should be vaccinated")

            if friend.get("wearing_a_mask") is False:
                masks_to_buy += 1

        if masks_to_buy > 0:
            raise NotWearingMaskError(f"Friends should buy "
                                      f"{masks_to_buy} masks")

    except NotWearingMaskError as e:
        return str(e)

    except VaccineError as e:
        return str(e)

    return f"Friends can go to {cafe.name}"
