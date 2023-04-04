from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count = 0
    count_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            count += 1
        except NotWearingMaskError:
            count_masks += 1
    if count > 0:
        return "All friends should be vaccinated"
    elif count_masks > 0:
        return f"Friends should buy {count_masks} masks"
    else:
        if isinstance(cafe, str):
            return f"Friends can go to {cafe}"
        return f"Friends can go to {cafe.name}"
