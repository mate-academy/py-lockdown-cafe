from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0  # how meny people without mask
    for friend in friends:
        try:
            # try to enter to cofe
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # count how many people without mask
            masks_to_buy += 1
    if masks_to_buy > 0:
        # how  many person without mask
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"  # every thing is good
