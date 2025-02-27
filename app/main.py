from app.cafe import Cafe
from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    all_friends_go = True
    masks_to_buy = 0

    for i, friend in enumerate(friends):
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            all_friends_go = False
        except NotWearingMaskError:
            masks_to_buy += 1

    if not all_friends_go:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
