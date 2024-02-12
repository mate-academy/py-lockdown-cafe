from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccine_to_do = 0
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError:
            vaccine_to_do += 1

    if vaccine_to_do > 0:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
