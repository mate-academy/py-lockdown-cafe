from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            without_mask += 1
        except VaccineError:
            return "All friends should be vaccinated"
    if without_mask:
        return f"Friends should buy {without_mask} masks"
    return f"Friends can go to {cafe.name}"
