from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe):
    count_friends_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_friends_masks += 1
    if count_friends_masks != 0:
        return f"Friends should buy {count_friends_masks} masks"
    return f"Friends can go to {cafe.name}"
