from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    count_friends = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            count_friends += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += +1
    if count_friends == len(friends):
        return f"Friends can go to {cafe.name}"
    elif masks_to_buy + count_friends == len(friends):
        return f"Friends should buy {masks_to_buy} masks"
