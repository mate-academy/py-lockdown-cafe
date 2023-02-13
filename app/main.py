from app.cafe import Cafe
from app.errors import (VaccineError, NotWearingMaskError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    friends_not_wearing_mask = 0
    invalid_vaccine = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            invalid_vaccine += 1
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            friends_not_wearing_mask += 1

    if friends_not_wearing_mask:
        return f"Friends should buy {friends_not_wearing_mask} masks"

    return f"Friends can go to {cafe.name}"
