import datetime
from app.cafe import Cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe):
    all_vaccinated = True
    masks_to_buy = 0
    outdated_vaccines = False

    for friend in friends:
        vaccine_info = friend.get("vaccine")
        wearing_mask = friend.get("wearing_a_mask", True)

        if not vaccine_info or vaccine_info.get("expiration_date") < datetime.date.today():
            raise NotVaccinatedError("All friends should be vaccinated")

        # expiration_date = vaccine_info.get("expiration_date")
        # if expiration_date and expiration_date < datetime.date.today():
        #     outdated_vaccines = True

        if not wearing_mask:
            masks_to_buy += 1
    #
    # if outdated_vaccines:
    #     raise OutdatedVaccineError("All friends should have up-to-date vaccines")

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
