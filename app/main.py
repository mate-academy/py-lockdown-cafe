from cafe import Cafe
from errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            mask_to_buy += 1
        except VaccineError:
            return "All friends should be vaccinated"

    if mask_to_buy > 0:
        mask_word = "mask" if mask_to_buy == 1 else "masks"
        return f"Friends should buy {mask_to_buy} {mask_word}"

    return f"Friends can go to {cafe.name}"
