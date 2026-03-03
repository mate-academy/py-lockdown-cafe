import datetime
from cafe import Cafe
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError

def go_to_cafe(friends, cafe: Cafe) -> str:
    # Check for each friend if they are allowed to visit the cafe
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError) as e:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    # If masks are required
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    # If all friends can go to the cafe
    return f"Friends can go to {cafe.name}"
