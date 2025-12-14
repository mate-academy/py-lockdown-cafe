import datetime
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError

def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_vaccinated = 0
    no_masks = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_vaccinated += 1
        except NotWearingMaskError:
            no_masks += 1

    if not_vaccinated > 0:
        return "All friends should be vaccinated"
    elif no_masks > 0:
        return f"Friends should buy {no_masks} masks"
    else:
        return f"Friends can go to {cafe.name}"
