import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends, cafe):
    try:
        for friend in friends:
            if "vaccine" not in friend:
                raise NotVaccinatedError("All friends should be vaccinated")

            vaccine_info = friend["vaccine"]
            expiration_date = vaccine_info.get("expiration_date")
            if not expiration_date or expiration_date < datetime.date.today():
                raise OutdatedVaccineError("All friends should be vaccinated")

            if not friend.get("wearing_a_mask"):
                raise NotWearingMaskError(friend["name"])

        return f"Friends can go to {cafe.name}"

    except (NotVaccinatedError, OutdatedVaccineError) as e:
        return str(e)
    except NotWearingMaskError as e:
        num_masks_to_buy = sum(1 for friend in friends if not friend.get("wearing_a_mask"))
        return f"Friends should buy {num_masks_to_buy} masks"
