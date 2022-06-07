from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe):
    masks_to_buy = 0
    mask_errors_count = 0
    guest = Cafe(cafe.name)
    for friend in friends:
        if friend['wearing_a_mask'] is False:
            masks_to_buy += 1
    for friend in friends:
        try:
            guest.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_errors_count += 1
    if mask_errors_count != 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
