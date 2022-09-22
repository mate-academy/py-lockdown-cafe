from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe):
    someone_is_not_vaccinated = False
    not_wearing_masks = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            someone_is_not_vaccinated = True
            break
        except NotWearingMaskError:
            not_wearing_masks += 1

    if someone_is_not_vaccinated:
        return "All friends should be vaccinated"

    if not_wearing_masks > 0:
        return f"Friends should buy {not_wearing_masks} masks"

    return f"Friends can go to {cafe.name}"
