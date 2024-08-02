from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_buy = 0
    friends_to_go_cafe = 0
    for friend in friends:
        try:
            if "Welcome" in cafe.visit_cafe(friend):
                friends_to_go_cafe += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_buy += 1
    if len(friends) == friends_to_go_cafe:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {masks_buy} masks"
