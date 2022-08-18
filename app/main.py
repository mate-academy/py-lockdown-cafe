import datetime
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends, cafe):
    count = 0
    for visitor in friends:
        if visitor["wearing_a_mask"] is False:
            count += 1
    try:
        for visitor in friends:
            if "vaccine" not in visitor.keys():
                raise NotVaccinatedError
    except NotVaccinatedError:
        return "All friends should be vaccinated"
    try:
        for visitor in friends:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError
    except OutdatedVaccineError:
        return "All friends should be vaccinated"
    try:
        for visitor in friends:
            if visitor["wearing_a_mask"] is False:
                raise NotWearingMaskError
    except NotWearingMaskError:
        return f"Friends should buy {count} masks"

    return f"Friends can go to {cafe.name}"
