import datetime
from datetime import date

from app.errors import OutdatedVaccineError, NotVaccinatedError, VaccineError, NotWearingMaskError
from app.cafe import Cafe

def go_to_cafe(friends: list, cafe: Cafe):
    count = 0
    for vaccinate_friend in friends:
        try:
            cafe.visit_cafe(vaccinate_friend)
        except (OutdatedVaccineError, NotVaccinatedError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count += 1

    if count > 0:
        return f"Friends should buy {count} masks"

    return f"Friends can go to {cafe.name}"

