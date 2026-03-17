from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    vaccinated = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                masks_to_buy += 1
        except VaccineError:
            pass
        else:
            vaccinated += 1

    if vaccinated < len(friends):
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
