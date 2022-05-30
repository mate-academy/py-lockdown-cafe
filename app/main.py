from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe):
    lacking_masks = 0
    allow = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            allow = False
            if not friend["wearing_a_mask"]:
                lacking_masks += 1
    if allow:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {lacking_masks} masks"
