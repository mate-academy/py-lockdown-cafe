from app.cafe import Cafe
from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError, NotWearingMaskError)
import datetime


def go_to_cafe(friends: list, cafe: Cafe) -> None | str:
    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except (OutdatedVaccineError, NotVaccinatedError):
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        try:
            for friend in friends:
                date_today = datetime.date.today()
                if "vaccine" not in friend:
                    raise NotVaccinatedError
                elif date_today > friend["vaccine"]["expiration_date"]:
                    raise OutdatedVaccineError
        except (OutdatedVaccineError, NotVaccinatedError):
            return "All friends should be vaccinated"
        else:
            list_of_not_wearing_mask = [friend for friend in friends
                                        if "wearing_a_mask" not in friend
                                        or friend["wearing_a_mask"] is False]
            counter = len(list_of_not_wearing_mask)
            return f"Friends should buy {counter} masks"
    else:
        return f"Friends can go to {cafe.name}"
