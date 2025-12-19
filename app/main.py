from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    count_of_friends_without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            count_of_friends_without_mask += 1
        except VaccineError:
            return "All friends should be vaccinated"

    if not count_of_friends_without_mask:
        return f"Friends can go to {cafe.name}"

    return f"Friends should buy {count_of_friends_without_mask} masks"
