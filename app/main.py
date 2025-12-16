from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_count = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError:
            return "All friends should be vaccinated"
        else:
            friends_count += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    if friends_count == len(friends):
        return f"Friends can go to {cafe.name}"
