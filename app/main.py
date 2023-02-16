from app.cafe import Cafe
from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    check = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
            check = False
        except NotWearingMaskError:
            masks_to_buy += 1
            check = False
    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"
    if check is True:
        return f"Friends can go to {cafe.name}"
