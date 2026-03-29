from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    counter_masks = 0
    flag = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            flag = False
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            counter_masks += 1
    if counter_masks > 0:
        return f"Friends should buy {counter_masks} masks"
    if flag:
        return f"Friends can go to {cafe.name}"
