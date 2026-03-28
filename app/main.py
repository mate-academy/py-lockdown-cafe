from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    correct_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
        else:
            correct_count += 1

    if correct_count == len(friends):
        return f"Friends can go to {cafe.name}"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
