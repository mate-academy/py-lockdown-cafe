from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    cafe = cafe
    friends_no_mask = 0
    perfect_friends = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            friends_no_mask += 1

        else:
            perfect_friends += 1
    if friends_no_mask > 0:
        return f"Friends should buy {friends_no_mask} masks"
    if perfect_friends == len(friends):
        return f"Friends can go to {cafe.name}"
