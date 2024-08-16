from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    without_a_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            without_a_mask += 1
    if without_a_mask > 0:
        return f"Friends should buy {without_a_mask} masks"
    return f"Friends can go to {cafe.name}"
