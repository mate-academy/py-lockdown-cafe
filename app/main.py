from typing import List
import datetime
from app import errors


def go_to_cafe(friends: List[dict], cafe: str) -> str:
    try:
        for friend in friends:
            vaccine_info = friend.get("vaccine")
            if not vaccine_info:
                raise errors.NotVaccinatedError(
                    "All friends should be vaccinated"
                )

            if vaccine_info["expiration_date"] < datetime.date.today():
                raise errors.OutdatedVaccineError(
                    "All friends should be vaccinated"
                )

        masks_to_buy = sum(
            1 for friend in friends
            if not friend.get("wearing_a_mask")
        )
        if masks_to_buy > 0:
            raise errors.NotWearingMaskError(
                f"Friends should buy {masks_to_buy} "
                f"masks"
            )

        return f"Friends can go to {cafe.name}"

    except errors.NotVaccinatedError as e:
        return str(e)
    except errors.OutdatedVaccineError as e:
        return str(e)
    except errors.NotWearingMaskError as e:
        return str(e)
