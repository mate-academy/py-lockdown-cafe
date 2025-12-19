from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: "Cafe") -> str:
    no_exception = True
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return ("All friends should be vaccinated")
            no_exception = False
        except NotWearingMaskError:
            masks_to_buy += 1
            no_exception = False

    if masks_to_buy > 0:
        return (f"Friends should buy {masks_to_buy} masks")

    if no_exception:
        return (f"Friends can go to {cafe.name}")
