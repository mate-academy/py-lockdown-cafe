from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    need_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            need_mask += 1
        except VaccineError:
            return "All friends should be vaccinated"
    if need_mask:
        return f"Friends should buy {need_mask} masks"
    return "Friends can go to KFC"
