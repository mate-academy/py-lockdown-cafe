from app.errors import NotWearingMaskError
from app.errors import VaccineError


def go_to_cafe(friends: list, cafe):
    count = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            count += 1
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count += 1
            masks_to_buy += 1
    if count == 0:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {masks_to_buy} masks"
