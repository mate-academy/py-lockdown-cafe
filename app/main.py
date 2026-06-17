from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str | None:
    masks_to_buy = 0
    not_exception = 0
    no_vaccine = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError:
            no_vaccine += 1
        else:
            not_exception += 1

    if no_vaccine:
        return "All friends should be vaccinated"
    elif not_exception == len(friends):
        return f"Friends can go to {cafe.name}"
    elif masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
