from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    vaccinated = True
    not_wearing_a_mask = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccinated = False
        except NotWearingMaskError:
            not_wearing_a_mask += 1

    if not vaccinated:
        return "All friends should be vaccinated"
    if not_wearing_a_mask > 0:
        return f"Friends should buy {not_wearing_a_mask} masks"

    return f"Friends can go to {cafe.name}"
