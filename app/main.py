from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list["dict"], cafe: Cafe) -> str:
    count_error_mask = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                count_error_mask += 1
    except VaccineError:
        return "All friends should be vaccinated"

    if count_error_mask != 0:
        return f"Friends should buy {count_error_mask} masks"

    return f"Friends can go to {cafe.name}"
