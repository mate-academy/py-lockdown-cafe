from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    needed_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All Friends should be vaccinated"
        except NotWearingMaskError:
            needed_mask += 1
    if needed_mask > 0:
        return f"Friends should buy {needed_mask} masks"
    else:
        return "Friends can go to KFC"
