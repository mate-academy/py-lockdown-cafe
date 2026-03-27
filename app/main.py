from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    vaccinated_friends = len(friends)
    friends_no_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccinated_friends -= 1
        except NotWearingMaskError:
            friends_no_mask += 1

    if len(friends) != vaccinated_friends:
        return "All friends should be vaccinated"
    elif friends_no_mask > 0:
        return f"Friends should buy {friends_no_mask} masks"
    return f"Friends can go to {cafe.name}"
