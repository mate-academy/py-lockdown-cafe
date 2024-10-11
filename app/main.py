from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    # Check each friend using try/except
    for friend in friends:
        try:
            # Try to allow the friend to visit the cafe
            cafe.visit_cafe(friend)
        except VaccineError:  # Removed 'as ve'
            # Catch both NotVaccinatedError and OutdatedVaccineError
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # Count how many friends are not wearing masks
            masks_to_buy += 1

    # If any friends don't have masks, return mask buying message
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    # If all friends are vaccinated and wearing masks
    return f"Friends can go to {cafe.name}"
