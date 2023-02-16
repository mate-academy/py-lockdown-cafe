from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_allowed = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            friends_allowed += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    if friends_allowed == len(friends):
        return f"Friends can go to {cafe.name}"
