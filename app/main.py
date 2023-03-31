from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_mask += 1
    if count_mask > 0:
        return f"Friends should buy {count_mask} masks"
    return f"Friends can go to {cafe.name}"
