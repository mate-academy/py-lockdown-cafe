from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_vaccinated = False
    masks_count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_vaccinated = True
        except NotWearingMaskError:
            masks_count += 1

    if not_vaccinated:
        return "All friends should be vaccinated"
    elif masks_count > 0:
        return f"Friends should buy {masks_count} masks"
    return f"Friends can go to {cafe.name}"
