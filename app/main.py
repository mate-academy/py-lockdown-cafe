from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccinated_friends = 0
    masks_to_buy = 0
    vaccine_errors = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            vaccinated_friends += 1
        except VaccineError:
            vaccine_errors += 1
        except NotWearingMaskError:
            masks_to_buy += 1

    if vaccine_errors > 0:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
