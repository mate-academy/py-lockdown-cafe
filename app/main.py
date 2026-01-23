from app.cafe import Cafe
from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> any:
    friends_list = []
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            friends_list.append(False)
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
            friends_list.append(False)
        else:
            friends_list.append(True)

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    if all(friends_list):
        return f"Friends can go to {cafe.name}"
