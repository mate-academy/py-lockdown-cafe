from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe):
    friend_without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            friend_without_mask += 1

    if friend_without_mask:
        return f"Friends should buy {friend_without_mask} masks"

    return f"Friends can go to {cafe.name}"
