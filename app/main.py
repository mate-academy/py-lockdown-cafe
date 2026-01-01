from cafe import Cafe
from errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_without_musks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            friends_without_musks += 1

    if friends_without_musks:
        return f"Friends should buy {friends_without_musks} masks"

    return f"Friends can go to {cafe.name}"
