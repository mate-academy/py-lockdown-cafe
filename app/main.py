from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friend_without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            friend_without_mask += 1
    if not friend_without_mask:
        return "Friends can go to KFC"
    return f"Friends should buy {friend_without_mask} masks"
