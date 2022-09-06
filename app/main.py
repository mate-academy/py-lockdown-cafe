from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe):
    need_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            need_masks += 1
    if need_masks > 0:
        return f"Friends should buy {need_masks} masks"
    return f"Friends can go to {cafe.name}"
