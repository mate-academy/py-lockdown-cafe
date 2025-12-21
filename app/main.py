from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_vaccinated = False
    not_wearing_masks = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_vaccinated = True
        except NotWearingMaskError:
            not_wearing_masks += 1

    if not_vaccinated:
        return "All friends should be vaccinated"
    elif not_wearing_masks > 0:
        return f"Friends should buy {not_wearing_masks} masks"
    else:
        return f"Friends can go to {cafe.name}"
