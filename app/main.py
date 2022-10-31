from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count = 0
    count_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            count_mask += 1

        else:
            count += 1

    if count_mask != 0:
        return f"Friends should buy {count_mask} masks"

    if count == len(friends):
        return "Friends can go to KFC"
