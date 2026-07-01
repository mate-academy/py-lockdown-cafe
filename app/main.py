from app.cafe import Cafe
from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    valid_vaccine = True

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError as e:
            print(e)
            masks_to_buy += 1
        except (NotVaccinatedError, OutdatedVaccineError) as e:
            print(e)
            valid_vaccine = False

    if valid_vaccine is False:
        message = "All friends should be vaccinated"
        return message
    elif masks_to_buy > 0:
        message = f"Friends should buy {masks_to_buy} masks"
        return message
    else:
        message = f"Friends can go to {cafe.name}"
        return message
