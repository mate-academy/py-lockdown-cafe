from app.cafe import Cafe
from app.errors import NotWearingMaskError
from app.errors import VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    friends_has_access = True
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            friends_has_access = False
            masks_to_buy += 1
        except VaccineError:
            return "All friends should be vaccinated"

    if friends_has_access:
        return f"Friends can go to {cafe.name}"

    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"
