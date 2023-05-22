from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_vaccine = 0
    count_masks = 0

    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            count_vaccine += 1
        except NotWearingMaskError:
            count_masks += 1

    if count_vaccine == 0 and count_masks == 0:
        return f"Friends can go to {cafe.name}"
    elif count_vaccine > 0:
        return "All friends should be vaccinated"
    else:
        return f"Friends should buy {count_masks} masks"
