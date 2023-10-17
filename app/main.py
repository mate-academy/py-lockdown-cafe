from app.errors import VaccineError, NotWearingMaskError

from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError as error:
            return f"{error}"
        except NotWearingMaskError:
            friends_without_mask += 1
    if friends_without_mask > 0:
        return f"Friends should buy {friends_without_mask} masks"
    return f"Friends can go to {cafe.name}"
