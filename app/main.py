from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    checked_friend = True

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            checked_friend = False
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            checked_friend = False
            masks_to_buy += 1

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    if checked_friend:
        return f"Friends can go to {cafe.name}"
