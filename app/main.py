from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe):
    masks_to_buy = 0

    for index, friend in enumerate(friends):
        try:
            cafe.visit_cafe(friend)

        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            masks_to_buy += 1

        else:
            if index == len(friends) - 1 and masks_to_buy == 0:
                return f"Friends can go to {cafe.name}"
            continue

    return f"Friends should buy {masks_to_buy} masks"
