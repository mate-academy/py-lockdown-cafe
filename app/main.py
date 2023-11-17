from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for i in range(len(friends)):
        try:
            cafe.visit_cafe(friends[i])
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError as e:
            return str(e)
        if i == len(friends) - 1 and masks_to_buy:
            return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
