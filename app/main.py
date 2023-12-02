from app.cafe import Cafe
from app.errors import VaccineError

from app.errors import NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    has_mask = True
    without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            has_mask = False
            without_mask += 1
    if not has_mask:
        return f"Friends should buy {without_mask} masks"
    return f"Friends can go to {cafe.name}"
