from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    all_vaccine = True
    all_mask = True
    friends_without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            all_vaccine = False
        except NotWearingMaskError:
            all_mask = False
            friends_without_mask += 1
    if all_vaccine is False:
        return "All friends should be vaccinated"
    if all_mask is False:
        return f"Friends should buy {friends_without_mask} masks"
    return f"Friends can go to {cafe.name}"
