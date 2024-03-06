from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccinated_friends = 0
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            vaccinated_friends += 1
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if vaccinated_friends == len(friends):
        if masks_to_buy > 0:
            return f"Friends should buy {masks_to_buy} masks"
        else:
            return f"Friends can go to {cafe.name}"
    else:
        return ("All friends should be vaccinated"
                if masks_to_buy == 0 else f"Friends should buy"
                                          f" {masks_to_buy} masks")
