from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_without_vaccine = 0
    friends_without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            friends_without_vaccine += 1
        except NotWearingMaskError:
            friends_without_mask += 1
    if friends_without_vaccine > 0:
        return "All friends should be vaccinated"
    if friends_without_vaccine == 0 and friends_without_mask > 0:
        return f"Friends should buy {friends_without_mask} masks"
    if friends_without_vaccine == 0 and friends_without_mask == 0:
        return f"Friends can go to {cafe.name}"
