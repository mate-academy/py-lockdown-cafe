from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_counter = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                masks_counter += 1
    except VaccineError:
        return "All friends should be vaccinated"
    if masks_counter:
        return f"Friends should buy {masks_counter} masks"
    return f"Friends can go to {cafe.name}"
