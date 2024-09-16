from app.cafe import Cafe

from app.errors import VaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe):
    masks_to_buy = 0
    counter = 0
    for human in friends:
        try:
            cafe.visit_cafe(human)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
        else:
            counter += 1
    if counter == len(friends):
        return f"Friends can go to {cafe.name}"
    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"
