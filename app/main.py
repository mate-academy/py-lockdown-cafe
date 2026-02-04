from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except VaccineError:
            # If anyone has a vaccine problem — stop immediately
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            # Count people without masks and keep checking others
            masks_to_buy += 1

    # After checking everyone:
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
