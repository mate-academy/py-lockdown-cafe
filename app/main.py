from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    counter = 0
    num_without_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            num_without_mask += 1
        else:
            counter += 1

    if num_without_mask >= 1:
        return f"Friends should buy {num_without_mask} masks"

    if counter == len(friends):
        return f"Friends can go to {cafe.name}"
