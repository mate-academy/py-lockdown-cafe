import datetime

from app.cafe import Cafe
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    sorted_friends = sorted(
        friends,
        key=lambda x:
        x.get("vaccine", {}).get("expiration_date", datetime.date.min))
    try:
        for friend in sorted_friends:
            cafe.visit_cafe(friend)
    except (NotVaccinatedError, OutdatedVaccineError):
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        masks_to_buy = sum(
            1 for friend in sorted_friends
            if not friend.get("wearing_a_mask", False)
        )
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
