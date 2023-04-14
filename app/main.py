from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    friends_not_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            friends_not_mask += 1
    if friends_not_mask > 0:
        return f"Friends should buy {friends_not_mask} masks"
    return f"Friends can go to {cafe.name}"
