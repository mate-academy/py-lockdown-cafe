from app.cafe import Cafe
from app.errors import NotWearingMaskError
from app.errors import VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_friends = 0
    masks_to_buy = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
        else:
            count_friends += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    if count_friends == len(friends):
        return f"Friends can go to {cafe.name}"
