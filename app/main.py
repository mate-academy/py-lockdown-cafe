from app.cafe import Cafe
from app.errors import NotWearingMaskError
from app.errors import VaccineError


def go_to_cafe(cafe: Cafe, friends: list) -> str:
    count_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_mask += 1
    if count_mask:
        return f"Friends should buy {count_mask} masks"
    return f"Friends can go to {cafe.name}"
