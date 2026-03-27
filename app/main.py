from app.cafe import Cafe
from app.errors import NotWearingMaskError
from app.errors import VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_count = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            friends_count += 1
        except VaccineError as e:
            return f"{e}"
        except NotWearingMaskError:
            masks_to_buy += 1
    if friends_count == len(friends):
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {masks_to_buy} masks"
