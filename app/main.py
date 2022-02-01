import app.errors as err
from app.cafe import Cafe


def go_to_cafe(cafe: Cafe, friends: list):
    mask_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except err.VaccineError:
            return 'All friends should be vaccinated'
        except err.NotWearingMaskError:
            mask_to_buy += 1

    if mask_to_buy:
        return f"Friends should buy {mask_to_buy} masks"
    return 'Friends can go to KFC'
