from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                    OutdatedVaccineError, NotWearingMaskError)
import datetime
date1 = datetime.date(2020, 3, 4)
date2 = datetime.date(2022, 1, 30)

assert  date1 < date2


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"


