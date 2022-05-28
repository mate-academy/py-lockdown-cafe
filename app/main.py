import datetime

from app.errors import NotVaccinatedError, NotWearingMaskError


def go_to_cafe(friends, cafe):
    mask_count = 0
    for friend in friends:
        if friend['wearing_a_mask'] is False:
            mask_count += 1
    for friend in friends:
        try:
            if "vaccine" not in friend or \
                    friend['vaccine']['expiration_date']\
                    < datetime.date.today():
                raise NotVaccinatedError("All friends should be vaccinated")
        except NotVaccinatedError:
            return "All friends should be vaccinated"
    for friend in friends:
        try:
            if friend['wearing_a_mask'] is False:
                raise NotWearingMaskError
        except NotWearingMaskError:
            return f"Friends should buy {mask_count} masks"
    return f"Friends can go to {cafe.name}"
