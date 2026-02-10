from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    all_vaccined = True
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            all_vaccined = False
            break
        except NotWearingMaskError:
            masks_to_buy += 1
    if all_vaccined and masks_to_buy == 0:
        return f"Friends can go to {cafe.name}"
    elif all_vaccined and masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return "All friends should be vaccinated"
