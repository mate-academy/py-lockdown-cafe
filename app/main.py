from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_without_mask = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except NotWearingMaskError:
            friends_without_mask += 1
        except VaccineError:
            return "All friends should be vaccinated"

    if friends_without_mask:
        return f"Friends should buy {friends_without_mask} masks"
    return "Friends can go to KFC"
