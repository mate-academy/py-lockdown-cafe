from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    correct_count = 0
    not_wearing_mask = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            correct_count += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            not_wearing_mask += 1
    if not_wearing_mask:
        return f"Friends should buy {not_wearing_mask} masks"
    if correct_count == len(friends):
        return f"Friends can go to {cafe.name}"
