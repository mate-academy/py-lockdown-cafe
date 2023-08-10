from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    allow_friend_count = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            allow_friend_count += 1
        except NotVaccinatedError as e:
            return str(e)
        except OutdatedVaccineError as e:
            return str(e)
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    if allow_friend_count == len(friends):
        return f"Friends can go to {cafe.name}"

    return ""
